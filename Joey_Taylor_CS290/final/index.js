function prependDesc(name, energy, power, desc) {
    return `${name} | Energy: ${energy} | Power: ${power} | ${desc}`
}

let collection = []


// Function to create and return a card element with attached data and event listeners.
function generateCardHTML(card) {
    const {name, effects, power, energy, img, series, desc, id} = card;
    const cardWrapper = document.createElement('div');
    if(effects.length) {
        effects.forEach(effect => {
            cardWrapper.dataset.effect = effect;
        });
    }
    cardWrapper.dataset.power = power;
    cardWrapper.dataset.energy = energy;
    cardWrapper.dataset.series = series;
    cardWrapper.dataset.name = name;
    cardWrapper.setAttribute("id", `card-id-${id}`);
    cardWrapper.style.backgroundImage=`url(${img})`;
    cardWrapper.classList.add("card-wrapper");

    const cardDesc = document.createElement('p');
    cardDesc.textContent = prependDesc(name, energy, power, desc);
    cardDesc.classList.add("card-desc");
    cardWrapper.appendChild(cardDesc);
    // Adds or removes cards from the collection and updates the button's state on click.
    cardWrapper.addEventListener('click', e => {
        const cardId = `card-id-${id}`;
        const collectionIndex = collection.indexOf(id);
        if(collectionIndex > -1) {
            collection.splice(collectionIndex, 1);
            e.currentTarget.classList.remove('added');
        } else {
            collection.push(id);
            e.currentTarget.classList.add('added');
        }
        const finalizeCollectionBtn = document.querySelector("#finalize-collection");
        if(collection.length > 0) {
            finalizeCollectionBtn.classList.remove("disabled");
        } else {
            finalizeCollectionBtn.classList.add("disabled");
        }
    });

    return cardWrapper;
}

const cardGrid = document.querySelector(".card-grid")

// Function to fetch card data, apply filters, and render the card elements on the page.
async function renderPage(filters=[]) {
    const rawData = await fetch("http://127.0.0.1:8000")
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

// Adds an event listener to the finalize collection button to redirect to the collection page.
const finalizeCollectionBtn = document.querySelector("#finalize-collection")
finalizeCollectionBtn.addEventListener('click', async e => {
    if(collection.length == 0) {
        e.target.classList.add("disabled")
        return
    }
    e.target.href = `./collection.html?collection=${collection}`
})

renderPage()