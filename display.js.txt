const data=
    [{
        "name": "ad hoc",
        "link": "https://www.youtube.com/embed/aU1EM4SSxQI"
    },
    {
        "name": "ad infinitum",
        "link": "https://www.youtube.com/embed/oSG1xo9mKto"
    },
    {
        "name": "add",
        "link": "https://www.youtube.com/embed/oJUjrqXkdjs"
    },
    {
        "name": "add",
        "link": "https://www.youtube.com/embed/lWnmHMNS06E"
    },
    {
        "name": "addict",
        "link": "https://www.youtube.com/embed/-5dVGIsVxeg"
    },
    {
        "name": "ademption",
        "link": "https://www.youtube.com/embed/pm4Dp34nkSY"
    },
    {
        "name": "adenoids",
        "link": "https://www.youtube.com/embed/3_coVAps7t0"
    },
    {
        "name": "adipsia",
        "link": "https://www.youtube.com/embed/mTUNdDVfA2w"
    },
    {
        "name": "adjourned and adjourned sine die",
        "link": "https://www.youtube.com/embed/6NoiCrItFV8"
    },
    {
        "name": "adjudge",
        "link": "https://www.youtube.com/embed/dCvX2SjAybM"
    },
    {
        "name": "administrative order",
        "link": "https://www.youtube.com/embed/oVRSWeU8r4I"
    },
    {
        "name": "administrator",
        "link": "https://www.youtube.com/embed/DLjKtmiEdVs"
    },
    {
        "name": "admire",
        "link": "https://www.youtube.com/embed/46-lhzhJf78"
    },
    {
        "name": "admonish",
        "link": "https://www.youtube.com/embed/pekDOgrcsjU"
    },
    {
        "name": "adopt",
        "link": "https://www.youtube.com/embed/Nqh6_B0gfec"
    },
    {
        "name": "adoption",
        "link": "https://www.youtube.com/embed/_svVSuoH6fo"
    },
    {
        "name": "adoptive child",
        "link": "https://www.youtube.com/embed/qI_HL9U9_UE"
    },
    {
        "name": "adoptive parent",
        "link": "https://www.youtube.com/embed/9Gb8falrx1Q"
    },
    {
        "name": "adult",
        "link": "https://www.youtube.com/embed/tjA2aFyBuY4"
    },
    {
        "name": "adulteration",
        "link": "https://www.youtube.com/embed/qq--OIvn7EY"
    }];

  newdata=JSON.stringify(data);
  finaldata=JSON.parse(newdata);
//  console.log(finaldata[0]["link"]);
  //finalData = newdata.replace(/\\/g, '');

let videoDiv = document.getElementsByClassName("video")[0];
console.debug(videoDiv);
finaldata.forEach(element => {
    let contentDiv = document.createElement("div");
    let videoFrame = document.createElement("iframe");
    let description = document.createElement("p");
    videoFrame.src = element.link;
    videoFrame.width="250";
    videoFrame.height="250";
    description.innerHTML=element.name;
    contentDiv.appendChild(videoFrame);
    contentDiv.appendChild(description);
    videoDiv.appendChild(contentDiv);
});
//   var items=document.getElementsByTagName('iframe');
//   console.log(items);
//   items.width="250";
//   items.height="250";
//   for(i=0;i<20;i++){
//     items[i].src=finaldata[i]["link"];
//   }
//   var descr=document.getElementsByClassName('desc');
//   console.log(descr);
