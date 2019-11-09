var Convert = {
    convertHtmlToCanvas: () => {
        return new Promise(resolve => {
            let $nav = $('#mainNav');
            $nav.hide();

            html2canvas(document.querySelector('html'))
            .then(canvas => {
                $nav.show();
                resolve(canvas);
            });
        });
    },

    convertCanvasToImage: (canvas) => {
        return canvas.toDataURL('image/png');
    }
}