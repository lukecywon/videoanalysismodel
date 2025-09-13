# CommentSense: AI-Powered Comment Analysis System

**Problem Statement**: Measuring content effectiveness through Share of Engagement (SoE) metrics like likes, shares, saves, and comments is essential. How do we analyze the quality and relevance of comments, at scale?

**Solution**: CommentSense provides a comprehensive AI-powered system for analyzing comment quality, sentiment, relevance, and engagement metrics.

By: **Noog Troupers**

## 🚀 Features

- **Quality Comment Ratio Analysis** - Identifies high vs low quality comments based on multiple factors
- **Sentiment Breakdown** - Positive, negative, neutral sentiment analysis per video
- **Comment Categorization** - Skincare, makeup, fragrance, and other categories
- **Spam Detection** - Advanced spam detection using multiple indicators
- **Relevance Analysis** - Measures comment relevance to video content using cosine similarity
- **Interactive Dashboard** - Visual analytics for easy interpretation
- **Per-Video Analytics** - Detailed breakdown for each video
- **KPI Tracking** - Key performance indicators for content effectiveness

## 📁 Project Structure

```
model_prototype/
├── model/                      # Core analysis modules
│   ├── __init__.py            # Package initialization
│   ├── dataset.py             # Data loading and management
│   ├── preprocessor.py        # Text preprocessing and spam detection
│   ├── sentiment_analysis.py  # Sentiment analysis using transformers
│   ├── relevance_analysis.py  # Comment-video relevance scoring
│   ├── video_analysis.py      # Video-level analytics and insights
│   ├── visualization.py       # Interactive dashboard creation
│   └── analytics.py           # KPI calculations and insights
├── main.py                    # Complete analysis pipeline
├── examples.py                # Usage examples for individual components
├── sample_analysis_model.ipynb # Original notebook implementation
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🛠️ Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download NLTK data (first run will do this automatically):
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
```

## 📖 Usage

### Quick Start - Full Pipeline

Run the complete analysis pipeline:

```python
python main.py
```

This will:
1. Load video and comment datasets
2. Preprocess and clean text
3. Analyze sentiment using RoBERTa model
4. Calculate relevance scores
5. Generate KPIs and insights
6. Create visualizations
7. Export results to CSV

### Individual Component Usage

```python
from model import (
    Dataset, 
    AdvancedTextPreprocessor, 
    SentimentAnalyzer,
    RelevanceAnalyzer,
    CommentAnalytics
)

# Load data
dataset = Dataset()
comments = dataset.getComments(dataset_id=1, sample_frac=0.1)

# Preprocess text
preprocessor = AdvancedTextPreprocessor()
comments["textCleaned"] = comments["textOriginal"].apply(preprocessor.clean_text)
comments["isSpam"] = comments["textOriginal"].apply(preprocessor.detect_spam)
comments["category"] = comments["textOriginal"].apply(preprocessor.categorize_comment)

# Analyze sentiment
sentiment_analyzer = SentimentAnalyzer()
sentiments, scores = sentiment_analyzer.analyze_sentiment(comments["textCleaned"].tolist())

# Calculate KPIs
analytics = CommentAnalytics()
kpis = analytics.calculate_kpis(comments)
insights = analytics.generate_insights(comments)
```

### Examples

Run the examples script to see individual component demonstrations:

```python
python examples.py
```

## 📊 Key Metrics and KPIs

### Quality Metrics
- **Quality Comment Ratio**: Percentage of high-quality comments
- **Spam Rate**: Percentage of detected spam comments
- **Average Relevance Score**: How well comments relate to video content

### Engagement Metrics
- **Sentiment Distribution**: Positive, negative, neutral percentages
- **Category Breakdown**: Skincare, makeup, fragrance comment distribution
- **Per-Video Performance**: Detailed analytics for each video

### Business Impact
- **Share of Engagement (SoE)** analysis through comment quality metrics
- **Scalable processing** with batch analysis for large datasets
- **Real-time insights** with actionable recommendations
- **Category-specific analysis** for targeted content strategy

## 🔧 Configuration

### Model Settings
- **Sentiment Model**: `cardiffnlp/twitter-roberta-base-sentiment-latest`
- **Device**: Automatically detects GPU/CPU
- **Batch Size**: Configurable for memory optimization

### Data Sources
- Comments: 5 CSV files from Google Cloud Storage
- Videos: Single CSV file with video metadata
- Sample fractions configurable for testing

### Translation Support (Optional)
Uncomment translation imports in `preprocessor.py` and install additional packages:
```bash
pip install googletrans langdetect
```

## 📈 Output Files

- `comment_analysis_results.csv`: Detailed analysis for each comment
- `video_analytics_summary.csv`: Per-video performance metrics
- Interactive visualizations (displayed in browser)

## 🎯 Use Cases

1. **Content Strategy Optimization**: Understand what content generates quality engagement
2. **Community Management**: Identify spam and low-quality comments for moderation
3. **Audience Insights**: Analyze sentiment and category preferences
4. **Performance Monitoring**: Track KPIs across different video types
5. **Competitive Analysis**: Compare engagement quality across channels

## 🤝 Contributing

This is a datathon prototype. For improvements:
1. Add more sophisticated spam detection algorithms
2. Implement multi-language support
3. Add real-time processing capabilities
4. Enhance visualization dashboards

## 📝 License

Developed for L'Oréal Datathon by Noog Troupers team.

## 🔍 Technical Details

### Architecture
- **Modular Design**: Each feature in separate, reusable modules
- **Scalable Processing**: Batch processing for large datasets
- **Error Handling**: Robust error handling throughout pipeline
- **Memory Efficient**: Optimized for processing large comment datasets

### AI Models
- **Sentiment Analysis**: Fine-tuned RoBERTa model for social media text
- **Relevance Scoring**: TF-IDF + Cosine similarity
- **Quality Assessment**: Multi-factor scoring algorithm
- **Spam Detection**: Pattern-based detection with multiple indicators

---

*CommentSense: Transforming comment data into actionable insights for content strategy optimization.*