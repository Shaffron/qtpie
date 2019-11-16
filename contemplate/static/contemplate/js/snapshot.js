var Snapshot = {
    takeShot: function (blur=false) {
        let targets = [
            '#mainNav',
            '#guide',
            '#pray',
            '#snapshot',
            '#word'
        ];

        this.hideUncapturedArea(targets);

        if (blur) {
            var $elem = $('.contemplate');
            this.blurContemplateArea($elem);
        }

        window.domtoimage
            .toJpeg(document.getElementById('body'), { quality: 1 })
            .then(dataUrl => {
                console.log(dataUrl);
                let link = document.createElement('a');
                let today = moment().format('YYYYMMDD');
                link.download = `Daily_QT_${today}.jpg`;
                link.href = dataUrl;
                link.click();
            })
            .finally(() => {
                Snapshot.showUncapturedArea(targets);
                if (blur) {
                    Snapshot.clearContemplateArea($elem);
                }
            });
    },

    takeBlurShot: function () {
        this.takeShot(blur=true);
    },

    hideUncapturedArea: function (targets) {
        for (target of targets) {
            $(target).hide();
        }
    },

    showUncapturedArea: function (targets) {
        for (target of targets) {
            $(target).show();
        }
    },

    blurContemplateArea: function ($elem) {
        $elem.css('filter', 'blur(2px)');
    },

    clearContemplateArea: function ($elem) {
        $elem.css('filter', '');
    },
};