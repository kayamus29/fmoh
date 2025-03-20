document.addEventListener("DOMContentLoaded", function() {
    var floatingBtn = document.getElementById("floatingBtn");
    var floatingCard = document.getElementById("floatingCard");
    var closeBtn = document.getElementById("closeBtn");
    
    // Show the card when the button is clicked
    floatingBtn.addEventListener("click", function() {
      floatingCard.style.display = "block";
    });
    
    // Hide the card when the close button is clicked
    closeBtn.addEventListener("click", function() {
      floatingCard.style.display = "none";
    });
    
    // Optionally hide the card if user clicks outside the card
    window.addEventListener("click", function(event) {
      if (event.target === floatingCard) {
        floatingCard.style.display = "none";
      }
    });
  });
  
  