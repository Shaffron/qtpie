var Convert = {
    convertHtmlToCanvas: (blur=false) => {
        return new Promise(resolve => {
            let targets = [
                '#mainNav',
                '#guide',
                '#pray',
                '#snapshot',
                '#word'
            ]

            Convert.hideUncapturedArea(targets);

            if (blur) {
                var $elem = $('.contemplate');
                Convert.blurContemplateArea($elem);
            }

            html2canvas(document.querySelector('html'))
            .then(canvas => {
                Convert.showUncapturedArea(targets);
                if (blur) {
                    Convert.clearContemplateArea($elem);
                }
                resolve(canvas);
            });
        });
    },

    convertCanvasToImage: (canvas) => {
        return canvas.toDataURL('image/png');
    },

    hideUncapturedArea: (targets) => {
        for (target of targets) {
            $(target).hide();
        }
    },

    showUncapturedArea: (targets) => {
        for (target of targets) {
            $(target).show();
        }
    },

    blurContemplateArea: ($elem) => {
        $elem.css('filter', 'blur(10px)');
    },

    clearContemplateArea: ($elem) => {
        $elem.css('filter', '');
    },
}