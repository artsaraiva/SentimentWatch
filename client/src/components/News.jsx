import React, { useContext, useState } from "react";
import moment from "moment";
import "moment/locale/en-gb";
import { NewsContext } from "../../contexts/NewsContext";
import Pagination from "./Pagination";
import Loading from "./Loading";
import cnnLogo from '../assets/cnn_logo.png';
import foxnewsLogo from '../assets/foxnews_logo.png';

const NewsPage = () => {
  const { newsItems, isLoading, filteredNewsItems } = useContext(NewsContext);

  const news = filteredNewsItems.length ? filteredNewsItems : newsItems;

  const itemsPerPage = 6;
  const [currentPage, setCurrentPage] = useState(1);
  const totalPages = Math.ceil(news.length / itemsPerPage);

  const handlePageChange = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const currentItems = news?.slice(startIndex, endIndex);

  const [showExplanation, setShowExplanation] = useState(false);
  const [explanationText, setExplanationText] = useState('');

  const handleExplanationClick = (explanation) => {
    setExplanationText(explanation);
    setShowExplanation(true);
  };

  const getSentimentClassificationAndEmoji = (score) => {
    if (score <= -0.8) return ["Overwhelmingly Negative", "🤬"];
    if (score <= -0.4) return ["Negative", "😠"];
    if (score <= -0.1) return ["Slightly Negative", "🙁"];
    if (score <= 0.1) return ["Neutral", "😐"];
    if (score <= 0.4) return ["Slightly Positive", "🙂"];
    if (score <= 0.8) return ["Positive", "😄"];
    return ["Overwhelmingly Positive", "😁"];
  };

  const getPlataformLogo = (plataform) => {
    console.log(plataform);
    if (plataform == 'CNN') return cnnLogo;
    if (plataform == 'FOXNEWS') return foxnewsLogo;
  }

  return (
    <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {showExplanation && (
        <div className="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-black bg-opacity-50 z-50">
          <div className="flex flex-col shadow-lg bg-gray-800 p-8 rounded-lg w-2/4">
            <div className="flex flex-row justify-between text-lg mb-2 text-white font-bold">
              <div>
                Text generated by OpenAI API
              </div>
              <button
                onClick={() => setShowExplanation(false)}
                className="flex justify-end font-bold text-lg mb-2 text-white font-bold text-3xl"
              >
                &times;
              </button>
            </div>
            <p className="text-white text-base">{explanationText}</p>
          </div>
        </div>
      )}

      {isLoading ? (
        <Loading />
      ) : (
        <>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 xl:gap-6">
            {currentItems.map((item) => (
              <div
                className="flex flex-col rounded-lg overflow-hidden shadow-lg bg-gray-800 hover:shadow-xl transition-all duration-300"
              >
                <div className="relative">
                  <div className="absolute top-0 left-0 z-10">
                    <img
                      src={getPlataformLogo(item.plataform)}
                      className="h-10"
                    />
                  </div>
                </div>
                <a href={item.postUrl} target="_blank" rel="noopener noreferrer">
                  <img
                    src={item.thumbnail}
                    className="w-full h-50 object-cover object-center"
                  />
                </a>
                <div className="p-4 flex-grow flex flex-col justify-between">
                  <h2 className="text-xl font-bold mb-2 text-white">{item.title}</h2>
                  <div className="flex flex-row justify-between items-end mt-2">
                    <div className="flex flex-col">
                      <p className="text-gray-400 text-sm font-bold mb-1">
                        {getSentimentClassificationAndEmoji(item.sentiment_score)[0]}:
                        <span className="emoji text-2xl">{getSentimentClassificationAndEmoji(item.sentiment_score)[1]}</span>
                      </p>
                      <div className="float left">
                        <button
                          onClick={() => handleExplanationClick(item.sentiment_explanation)}
                          className="border border-blue-500 text-blue-500 py-2 px-4 rounded-md hover:bg-blue-500 hover:text-white transition-all duration-200"
                        >
                          Show Explanation
                        </button>
                      </div>
                    </div>
                    <div className="flex flex-col justify-end items-end mt-2">
                      <p className="text-gray-400 text-sm font-bold mb-1">
                        {moment(item.published_date).fromNow()}
                      </p>
                      <a
                        href={item.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="border border-blue-500 text-blue-500 py-2 px-4 rounded-md hover:bg-blue-500 hover:text-white transition-all duration-200"
                      >
                        Read More
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
          <Pagination
            currentPage={currentPage}
            handlePageChange={handlePageChange}
            totalPages={totalPages}
          />
        </>
      )}
    </div>
  );
};

export default NewsPage;