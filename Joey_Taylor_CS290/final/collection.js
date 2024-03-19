function prependDesc(name, energy, power, desc) {
    return `${name} | Energy: ${energy} | Power: ${power} | ${desc}`
}


// Function to create and return a card element with attached data and event listeners.
function generateCardHTML(card) {
    const {name, effects, power, energy, img, series, desc, id} = card
    const cardWrapper = document.createElement('div')
    if(effects.length) {
        effects.forEach(effect => {
            cardWrapper.dataset.effect = effect
        })
    }
    cardWrapper.dataset.power = power
    cardWrapper.dataset.energy = energy
    cardWrapper.dataset.series = series
    cardWrapper.dataset.name = name
    cardWrapper.setAttribute("id", `card-id-${id}`)
    cardWrapper.style.backgroundImage=`url(${img})`
    cardWrapper.classList.add("card-wrapper")

    const cardDesc = document.createElement('p')
    cardDesc.textContent = prependDesc(name, energy, power, desc)
    cardDesc.classList.add("card-desc")
    cardWrapper.appendChild(cardDesc)   
    return cardWrapper
}

const cardGrid = document.querySelector(".card-grid")


// Function to fetch card data, apply filters, and render the card elements on the page.
async function renderPage() {
    const collection = [...window.location.href.split("=")[1].split(',')].map(num => Number(num))
    const rawData = await fetch(`http://localhost:8000/collection?collection=${collection}`)
    const data = await rawData.json()
            
    cardGrid.innerHTML = ""
    if(filters.length > 0) {
        const filteredData = data.filter(card => filters.some(filter => filter == card.series || (card.effects.length > 0 ? card.effects.includes(filter) : false)))
        filteredData.forEach(card => {
            cardGrid.appendChild(generateCardHTML(card))
        })
    } else {
        data.forEach(card => {
            cardGrid.appendChild(generateCardHTML(card))
        })
    }
}


// Adds event listeners to filter inputs to update the page with filtered card data.
const filters = []
const allFilters = [...document.querySelectorAll(".filter input")]
allFilters.forEach(filter => {
    filter.addEventListener('click', async e => {
        const val = e.target.value
        if(e.target.checked) {
            filters.push(val)
        } else {
            const idx = filters.indexOf(val)
            if(idx > -1) {
                filters.splice(idx, 1)
            }
        }
        await renderPage(filters)
    })
})


renderPage()