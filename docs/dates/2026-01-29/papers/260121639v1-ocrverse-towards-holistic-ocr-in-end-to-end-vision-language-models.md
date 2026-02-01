---
layout: default
title: OCRVerse: Towards Holistic OCR in End-to-End Vision-Language Models
---

# OCRVerse: Towards Holistic OCR in End-to-End Vision-Language Models
**arXiv**：[2601.21639v1](https://arxiv.org/abs/2601.21639) · [PDF](https://arxiv.org/pdf/2601.21639.pdf)  
**作者**：Yufeng Zhong, Lei Chen, Xuanle Zhao, Wenkang Han, Liming Zheng, Jing Huang, Deyang Jiang, Yilin Cao, Lin Ma, Zhixiong Zeng  

**一句话要点**：提出OCRVerse，一种端到端视觉语言模型中的整体OCR方法，统一文本中心与视觉中心OCR。

**关键词**：整体OCR, 端到端视觉语言模型, 多域训练, 文本中心OCR, 视觉中心OCR, SFT-RL方法

## 3 点简述
- 现有OCR方法主要关注文本识别，忽视图表、网页等视觉信息密集图像的识别需求。
- OCRVerse通过综合数据工程和两阶段SFT-RL多域训练方法，实现跨域统一处理。
- 实验显示OCRVerse在文本和视觉中心数据类型上取得竞争性结果，媲美大型开源和闭源模型。

## 摘要（原文）

> The development of large vision language models drives the demand for managing, and applying massive amounts of multimodal data, making OCR technology, which extracts information from visual images, increasingly popular. However, existing OCR methods primarily focus on recognizing text elements from images or scanned documents (\textbf{Text-centric OCR}), neglecting the identification of visual elements from visually information-dense image sources (\textbf{Vision-centric OCR}), such as charts, web pages and science plots. In reality, these visually information-dense images are widespread on the internet and have significant real-world application value, such as data visualization and web page analysis. In this technical report, we propose \textbf{OCRVerse}, the first holistic OCR method in end-to-end manner that enables unified text-centric OCR and vision-centric OCR. To this end, we constructe comprehensive data engineering to cover a wide range of text-centric documents, such as newspapers, magazines and books, as well as vision-centric rendered composites, including charts, web pages and scientific plots. Moreover, we propose a two-stage SFT-RL multi-domain training method for OCRVerse. SFT directly mixes cross-domain data to train and establish initial domain knowledge, while RL focuses on designing personalized reward strategies for the characteristics of each domain. Specifically, since different domains require various output formats and expected outputs, we provide sufficient flexibility in the RL stage to customize flexible reward signals for each domain, thereby improving cross-domain fusion and avoiding data conflicts. Experimental results demonstrate the effectiveness of OCRVerse, achieving competitive results across text-centric and vision-centric data types, even comparable to large-scale open-source and closed-source models.

