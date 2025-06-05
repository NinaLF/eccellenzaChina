
const behaviorData = {

    "<b>Diet </b> <br> Based on an average adults' caloric needs for the duration of one year": {
                "Meat-based": 2.206,
                "Vegetarian ": 1.338
                
    },
    "<b>Drying clothes</b> <br> based on 3 drying loads per week and the average energy mix": {
                "air dry clothers": 0.0,
                "use dryer (average dryer and full load)": 0.039
    },
    "<b>Recycling</b>  <br>  Materials such as paper, glass, metals for one year ": {
                "Does not recycle": 0.0575,
                "Recycles": 0.0
    },
    "<b>Food</b>  <br>Foods and bevarages bought and consumed for one year ": {
                "more than 3/4 is regional": 0.0,
                "more than 3/4 is imported": 0.44
    },
    "<b>Commute</b> <br> 12.5 miles to and from work everyday (one trip = 6.25 miles), 5 days a week for 48 weeks per year": {
                "by bus": 0.471,
                "by car": 1.595
    },
    "<b>Travel to go on vacation</b>   ": {
                "1 round-trip 3-6 hour flight (=2 flights)": 1.2,
                "via train (does not fly)": 0.0076
    }

};

function createBehaviorSelectors() {
    const behaviorsDiv = document.getElementById('behaviors');
    for (let behavior in behaviorData) {
        const container = document.createElement('div');
        container.className = 'behavior-container';
        
        const label = document.createElement('label');
        label.innerText = behavior;
        label.className = 'behavior-label';
        container.appendChild(label);
        
        const select = document.createElement('select');
        select.dataset.behavior = behavior;
        select.onchange = updateTotalFootprint;
        
        for (let level in behaviorData[behavior]) {
            const option = document.createElement('option');
            option.value = behaviorData[behavior][level];
            option.innerText = level;
            select.appendChild(option);
        }
        
        container.appendChild(select);
        behaviorsDiv.appendChild(container);
    }
}

// Function to update the total carbon footprint
function updateTotalFootprint() {
    let totalFootprint = 0.0;
    const selects = document.querySelectorAll('select');
    selects.forEach(select => {
        totalFootprint += parseFloat(select.value);
    });
    document.getElementById('total-footprint').innerText = totalFootprint.toFixed(1);
}

// Initialize the behavior selectors on page load
window.onload = createBehaviorSelectors;
