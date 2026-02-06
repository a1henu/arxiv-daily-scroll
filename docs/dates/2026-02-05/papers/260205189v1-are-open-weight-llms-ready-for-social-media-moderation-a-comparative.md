---
layout: default
title: Are Open-Weight LLMs Ready for Social Media Moderation? A Comparative Study on Bluesky
---

# Are Open-Weight LLMs Ready for Social Media Moderation? A Comparative Study on Bluesky
**arXiv**：[2602.05189v1](https://arxiv.org/abs/2602.05189) · [PDF](https://arxiv.org/pdf/2602.05189.pdf)  
**作者**：Hsuan-Yu Chou, Wajiha Naveed, Shuyan Zhou, Xiaowei Yang  

**一句话要点**：评估开源权重大语言模型在Bluesky社交媒体内容审核中的性能，并与专有模型比较。

**关键词**：社交媒体审核, 大语言模型, 开源权重模型, 有害内容检测, 隐私保护, 模型比较

## 3 点简述
- 核心问题：开源权重LLMs在社交媒体内容审核中的开箱即用能力是否与专有模型相当。
- 方法要点：在Bluesky平台上测试七种先进LLMs，包括四种专有和三种开源权重模型，使用真实帖子和人工标注。
- 实验或效果：开源权重模型在敏感性和特异性上与专有模型有显著重叠，支持隐私保护审核，并揭示不同有害内容类型的检测差异。

## 摘要（原文）

> As internet access expands, so does exposure to harmful content, increasing the need for effective moderation. Research has demonstrated that large language models (LLMs) can be effectively utilized for social media moderation tasks, including harmful content detection. While proprietary LLMs have been shown to zero-shot outperform traditional machine learning models, the out-of-the-box capability of open-weight LLMs remains an open question.
>   Motivated by recent developments of reasoning LLMs, we evaluate seven state-of-the-art models: four proprietary and three open-weight. Testing with real-world posts on Bluesky, moderation decisions by Bluesky Moderation Service, and annotations by two authors, we find a considerable degree of overlap between the sensitivity (81%--97%) and specificity (91%--100%) of the open-weight LLMs and those (72%--98%, and 93%--99%) of the proprietary ones. Additionally, our analysis reveals that specificity exceeds sensitivity for rudeness detection, but the opposite holds for intolerance and threats. Lastly, we identify inter-rater agreement across human moderators and the LLMs, highlighting considerations for deploying LLMs in both platform-scale and personalized moderation contexts. These findings show open-weight LLMs can support privacy-preserving moderation on consumer-grade hardware and suggest new directions for designing moderation systems that balance community values with individual user preferences.

