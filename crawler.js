const Crawler = require("crawler");
const fs = require("fs");

module.exports = function (param = "") {
    Arr = [];

    const c = new Crawler({
        maxConnections: 10,
        callback: function (error, res, done) {
            if (error) {
                console.log(error);
                done();
            }

            fuSelector(res, Arr);

            fs.writeFileSync(
              param === "" ? "json/index.json" : "json/search.json",
              JSON.stringify(Arr)
            );

            done();
        },
    });

    const fuSelector = (res, Arr) => {
        const $ = res.$;
        $(".photo-grid-item")
            .find("a img")
            .each((index, item) => {
                let photo =
                    item.attribs.src === undefined
                        ? item.attribs["data-cfsrc"]
                        : item.attribs.src;

                obj = {
                    photo: photo.includes("https://cdn.stocksnap.io/") ? photo : "",
                    width: item.attribs.width,
                    height: item.attribs.height,
                    description:
                        item.attribs.alt === undefined ? "unknown" : item.attribs.alt,
                };

                Arr.push(obj);
            });
    };

    c.queue("https://stocksnap.io/" + param);
};
