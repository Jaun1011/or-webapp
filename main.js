

const or = JSON.parse(localStorage.getItem("or"))

const articleView = article => `
    <li class="article">
        <strong>${article.article}</strong>
        <div>${article.content}</div>
    </li>
`


const projectArticles = searchBar => {

    const rootElement = document.createElement("div");

    searchBar.addEventListener("input", _ => {

        const articles = or
            .filter(a => a.content.includes(searchBar.value))
            .map(articleView)
            .join("");
    
        
        rootElement.innerHTML = `
            <ul class="articles">${articles}</ul>
        `;
    });

    const articles = or.map(articleView).join("");
    
    rootElement.innerHTML += `
        <ul class="articles">${articles}</ul>
    `;


    return rootElement;
}

const searchBarProjector = _ => {

    const searchBar = document.createElement("input");
    searchBar.setAttribute("id", "searchbar");
    searchBar.setAttribute("type", "text");
    
    return searchBar; 
}





const projectOrApp = rootElement => {
    const searchbar = searchBarProjector();

    rootElement.appendChild(searchbar);
    rootElement.appendChild(projectArticles(searchbar));
}

projectOrApp(document.getElementById("or-app"))