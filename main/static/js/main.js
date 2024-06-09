// main.js

function showDetails(type) {
    console.log('Image clicked:', type); // Debug log

    const detailsContainer = document.getElementById('details-container');

    // Clear previous content
    detailsContainer.innerHTML = '';

    // Create new wrapper
    const whiteWrapper = document.createElement('div');
    whiteWrapper.className = 'white-wrapper';

    // Add content based on the clicked image
    if (type === 'class2') {
        whiteWrapper.innerHTML = `
            <div class="white-content">
                <h3>Class 2 Details</h3>
                <p>This is where the details for Class 2 will be displayed.</p>
            </div>
        `;
    } else if (type === 'class1') {
        whiteWrapper.innerHTML = `
            <div class="white-content">
                <h3>Class 1 Details</h3>
                <p>This is where the details for Class 1 will be displayed.</p>
            </div>
        `;
    }

    // Append the new wrapper to the details container
    detailsContainer.appendChild(whiteWrapper);
}
