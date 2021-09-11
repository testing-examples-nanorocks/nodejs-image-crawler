const Crawler = require("crawler");
const fs = require("fs");
const NodeCache = require("node-cache");
const myCache = new NodeCache();

module.exports = function (param = "", response, flag='index') {

    if (myCache.has(flag)) {
      response.json(myCache.take(flag));
      return;
    } 
    
    Arr = [];

    const c = new Crawler({
        maxConnections: 10,
        callback: function (error, res, done) {
            if (error) {
                console.log(error);
                done();
            }

            fuSelector(res, Arr);
            console.log('We crawl again !!!');
            myCache.set(flag, Arr, 20000);
            response.json(Arr);

            done();
        },
    });

    const fuSelector = (res, Arr) => {
        const $ = res.$;
        $(".photo-grid-item")
            .find("a img")
            .each((index, item) => {

                if(index % 2 !== 0)
                {
                    return;
                }

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
