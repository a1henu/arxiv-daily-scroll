---
layout: default
title: A Unified XAI-LLM Approach for EndotrachealSuctioning Activity Recognition
---

# A Unified XAI-LLM Approach for EndotrachealSuctioning Activity Recognition
**arXiv**：[2601.21802v1](https://arxiv.org/abs/2601.21802) · [PDF](https://arxiv.org/pdf/2601.21802.pdf)  
**作者**：Hoang Khang Phan, Quang Vinh Dang, Noriyo Colley, Christina Garcia, Nhat Tan Le  

**一句话要点**：提出统一XAI-LLM框架以解决气管内吸痰活动识别与反馈生成问题

**关键词**：活动识别, 可解释人工智能, 大型语言模型, 视频分析, 医疗教育, 反馈生成

## 3 点简述
- 核心问题：气管内吸痰活动识别在家庭护理和教育场景中缺乏自动化系统，监督有限。
- 方法要点：以大型语言模型为核心，从视频数据执行时空活动识别和可解释决策分析。
- 实验或效果：LLM方法在准确率和F1分数上比基线模型提升约15-20%，并集成异常检测和XAI提供反馈。

## 摘要（原文）

> Endotracheal suctioning (ES) is an invasive yet essential clinical procedure that requires a high degree of skill to minimize patient risk - particularly in home care and educational settings, where consistent supervision may be limited. Despite its critical importance, automated recognition and feedback systems for ES training remain underexplored. To address this gap, this study proposes a unified, LLM-centered framework for video-based activity recognition benchmarked against conventional machine learning and deep learning approaches, and a pilot study on feedback generation. Within this framework, the Large Language Model (LLM) serves as the central reasoning module, performing both spatiotemporal activity recognition and explainable decision analysis from video data. Furthermore, the LLM is capable of verbalizing feedback in natural language, thereby translating complex technical insights into accessible, human-understandable guidance for trainees. Experimental results demonstrate that the proposed LLM-based approach outperforms baseline models, achieving an improvement of approximately 15-20\% in both accuracy and F1 score. Beyond recognition, the framework incorporates a pilot student-support module built upon anomaly detection and explainable AI (XAI) principles, which provides automated, interpretable feedback highlighting correct actions and suggesting targeted improvements. Collectively, these contributions establish a scalable, interpretable, and data-driven foundation for advancing nursing education, enhancing training efficiency, and ultimately improving patient safety.

