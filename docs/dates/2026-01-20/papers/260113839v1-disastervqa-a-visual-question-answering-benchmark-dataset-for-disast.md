---
layout: default
title: DisasterVQA: A Visual Question Answering Benchmark Dataset for Disaster Scenes
---

# DisasterVQA: A Visual Question Answering Benchmark Dataset for Disaster Scenes
**arXiv**：[2601.13839v1](https://arxiv.org/abs/2601.13839) · [PDF](https://arxiv.org/pdf/2601.13839.pdf)  
**作者**：Aisha Al-Mohannadi, Ayisha Firoz, Yin Yang, Muhammad Imran, Ferda Ofli  

**一句话要点**：提出DisasterVQA基准数据集，用于评估灾难场景下的视觉问答模型性能。

**关键词**：视觉问答, 灾难响应, 基准数据集, 情境感知, 模型评估, 人道主义框架

## 3 点简述
- 核心问题：现有视觉问答模型在灾难响应中的复杂推理能力未知，需专门评估。
- 方法要点：构建包含1,395张真实图像和4,405个专家标注问答对的数据集，基于人道主义框架设计问题。
- 实验或效果：测试七个先进模型，发现其在二元问题表现好，但在细粒度推理和少数灾难场景中表现不佳。

## 摘要（原文）

> Social media imagery provides a low-latency source of situational information during natural and human-induced disasters, enabling rapid damage assessment and response. While Visual Question Answering (VQA) has shown strong performance in general-purpose domains, its suitability for the complex and safety-critical reasoning required in disaster response remains unclear. We introduce DisasterVQA, a benchmark dataset designed for perception and reasoning in crisis contexts. DisasterVQA consists of 1,395 real-world images and 4,405 expert-curated question-answer pairs spanning diverse events such as floods, wildfires, and earthquakes. Grounded in humanitarian frameworks including FEMA ESF and OCHA MIRA, the dataset includes binary, multiple-choice, and open-ended questions covering situational awareness and operational decision-making tasks. We benchmark seven state-of-the-art vision-language models and find performance variability across question types, disaster categories, regions, and humanitarian tasks. Although models achieve high accuracy on binary questions, they struggle with fine-grained quantitative reasoning, object counting, and context-sensitive interpretation, particularly for underrepresented disaster scenarios. DisasterVQA provides a challenging and practical benchmark to guide the development of more robust and operationally meaningful vision-language models for disaster response. The dataset is publicly available at https://zenodo.org/records/18267770.

