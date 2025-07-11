import Header from "../components/Header";
import React, { useState, useRef, useEffect } from "react";
import axios from "axios";
import CharacterCard from "../components/CharacterCard";
import Button from "react-bootstrap/Button"; // can also import Col, Row from "react-bootstrap" if needed
import CharacterSearch from "../components/CharacterSearch";

export default function Characters() {
    const [characters, setCharacters] = useState([]);
    const inputRef = useRef(null); // Create a ref for the input field

    const handleSearch = async() => {
        await CharacterSearch(inputRef, characters, setCharacters);
    }

    return (
        <>
            <Header />
            <div className="characters-page flex flex-col items-center">
                <h1>Characters Page</h1>
                {/* Search Input */}
                <input
                    type="text" 
                    placeholder="Search for a character..." 
                    className="charSearch text-center" 
                    ref={inputRef} // Attach the ref to the input field
                />

                {/* Search Button */}
                <Button onClick={handleSearch}>Search</Button>

                {/* Character Cards */}
                {characters.length > 0 && characters.map(character => (
                    <CharacterCard key={character.id} character={character} />))}

                {characters.length === 0 && <p>No characters found. Please try a different search.</p>}
            </div>
        </>
    );
}