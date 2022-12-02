const TIME = 1000 * 60; // 60 seconds

function refresh() {
    setInterval(function() {
        window.location.reload();
    }, TIME);
}

function main() {
    refresh();
}

main();