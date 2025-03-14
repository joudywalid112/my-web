function calculateResult() {
    let form = document.getElementById("autismTest");
    let score = 0;
    let totalQuestions = 3;

    for (let i = 1; i <= totalQuestions; i++) {
        score += parseInt(form["q" + i].value);
    }

    let percentage = (score / (totalQuestions * 5)) * 100;
    localStorage.setItem("autismScore", percentage.toFixed(2));

    window.location.href = "result.html";
}
