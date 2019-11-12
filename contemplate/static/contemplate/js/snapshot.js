var Snapshot = {
    takeShot: () => {
        let promise = Convert.convertHtmlToCanvas();

        promise.then(canvas => {
            let image = Convert.convertCanvasToImage(canvas);
            Snapshot.downloadImage(image);
        });
    },

    takeBlurShot: () => {
        let promise = Convert.convertHtmlToCanvas(true);

        promise.then(canvas => {
            let image = Convert.convertCanvasToImage(canvas);
            Snapshot.downloadImage(image);
        });
    },

    downloadImage: (image) => {
        let link = document.createElement('a');
        link.href = image;
        link.download = 'TodayQT.png';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        delete link;
    }
}