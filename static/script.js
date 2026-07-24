document.addEventListener("DOMContentLoaded", () => { // dome이 다 그려졌을 때 아래 fetch 실행
    fetch("/api/data")
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("result").textContent = data.message;  // index.html에 result가 있음
        })
        .catch((error) => {
            document.getElementById("result").textContent = "데이터 불러오기 실패";
            console.error(error);
        });
});