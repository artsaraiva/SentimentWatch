import React, { useContext, useState } from "react";
import { NewsContext } from "../../contexts/NewsContext";

function Navbar() {
  const { setSearchQuery, searchQuery } = useContext(NewsContext);

  const handleSearch = (e) => {
    setSearchQuery(e.target.value);
  };

  const [showExplanation, setShowExplanation] = useState(false);
  const [explanationText, setExplanationText] = useState('');

  const handleExplanationClick = (explanation) => {
    setExplanationText(explanation);
    setShowExplanation(true);
  };

  const howItWorksText = 'The app extracts the text of each RSS feed with web scraping techniques. The article text is then submitted to'
  + ' the OpenAI API through a prompt that determines the sentiment of the article. Then, based on the score given by the AI, it is'
  + ' classified this way:<br><br>'
  + '🤬 Overwhelmingly Negative: -1 to -0.8<br>'
  + '😠 Negative: -0.8 to -0.4<br>'
  + '🙁 Slightly Negative: -0.4 to -0.1<br>'
  + '😐 Neutral: -0.1 to 0.1<br>'
  + '🙂 Slightly Positive: 0.1 to 0.4<br>'
  + '😄 Positive: 0.4 to 0.8<br>'
  + '😁 Overwhelmingly Positive: 0.8 to 1';

  return (
    <nav className="flex items-center justify-between flex-wrap bg-gray-800 p-2">
      {showExplanation && (
        <div className="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-black bg-opacity-50 z-50">
          <div className="flex flex-col shadow-lg bg-gray-800 p-8 rounded-lg w-2/4">
            <div className="flex flex-row justify-between">
              <div className="text-xl mb-2 text-white font-bold">
                How it all works
              </div>
              <button
                onClick={() => setShowExplanation(false)}
                className="flex justify-end font-bold text-lg mb-2 text-white font-bold text-3xl"
              >
                &times;
              </button>
            </div>
            <p className="text-white text-base" dangerouslySetInnerHTML={{ __html: howItWorksText }} />
          </div>
        </div>
      )}
      <div className="flex items-center flex-shrink-0 text-white mr-6">
        <a
          href="/"
          className="text-xl font-bold cursor-pointer text-white transition-all duration-500 hover:text-blue-500"
        >
          SentimentWatch
        </a>
      </div>
      <div className="h-30 flex flex-row">
        <div className="flex items-center justify-center p-2">
          <a
            onClick={() => handleExplanationClick(howItWorksText)}
            className="text-gl font-lighter cursor-pointer text-white transition-all duration-500 hover:text-blue-500"
          >
            How it works
          </a>
        </div>
        <form className="w-80 max-w-sm p-2">
          <div className="flex items-center border-b-2 border-blue-500 py-2">
            <input
              className="appearance-none bg-transparent border-none w-full text-white mr-3 py-1 px-1 leading-tight focus:outline-none"
              type="text"
              placeholder="Search"
              value={searchQuery}
              onChange={handleSearch}
            />
          </div>
        </form>
      </div>
    </nav>
  );
}

export default Navbar;
