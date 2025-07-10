import Header from "../components/Header";

export default function Characters() {
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