import axios from "axios";

const CharacterSearch = async(inputRef, characters, setCharacters) => {
        if (inputRef.current.value === "") {
            alert("Please enter a character name to search.");
            return;
        }
        if (characters.length > 0) {
            // Clear previous characters if any
            setCharacters([]);
        }
        const response = await axios.get(`https://rickandmortyapi.com/api/character/?name=${inputRef.current.value}`);
        setCharacters([...characters, ...response.data.results]);
}

export default CharacterSearch;