document.addEventListener('DOMContentLoaded', (event) => {
    const bodyClasses = ['bodyColor1', 'bodyColor2', 'bodyColor3', 'bodyColor4'];
    const infoBoxClasses = ['info-boxColor1', 'info-boxColor2', 'info-boxColor3', 'info-boxColor4'];
    let currentColorIndex = 0; // Start with the first color

    // This assumes you have a button with the ID 'changeColor' in your HTML
    document.getElementById('changeColor').addEventListener('click', function() {
        // Remove the old body color class
        document.body.classList.remove(bodyClasses[currentColorIndex]);
        document.querySelector('.info-box').classList.remove(infoBoxClasses[currentColorIndex]);

        // Move to the next color
        currentColorIndex = (currentColorIndex + 1) % bodyClasses.length;

        // Add the new body color class
        document.body.classList.add(bodyClasses[currentColorIndex]);
        document.querySelector('.info-box').classList.add(infoBoxClasses[currentColorIndex]);
    });
    });
