import Header from "../components/Header";
import React, { useState, useEffect } from "react";
import axios from "axios";

export default function Characters() {
    const [characters, setCharacters] = useState([]);

    const fetchCharacters = async() => {
        response = await axios.get("https://rickandmortyapi.com/api/character");
        console.log(response.data);
    }

    return (
        <>
            <Header />
            <div className="characters-page">
                <h1>Characters Page</h1>
                <p>This is the Characters page where you can find information about various characters from the Rick and Morty universe.</p>
                {/* You can add more content or components related to characters here */}
            </div>
        </>
    );
}