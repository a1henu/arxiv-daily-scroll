---
layout: default
title: SAM Audio Judge: A Unified Multimodal Framework for Perceptual Evaluation of Audio Separation
---

# SAM Audio Judge: A Unified Multimodal Framework for Perceptual Evaluation of Audio Separation
**arXiv**：[2601.19702v1](https://arxiv.org/abs/2601.19702) · [PDF](https://arxiv.org/pdf/2601.19702.pdf)  
**作者**：Helin Wang, Bowen Shi, Andros Tjandra, John Hoffman, Yi-Chiao Wu, Apoorv Vyas, Najim Dehak, Ann Lee, Wei-Ning Hsu  

**一句话要点**：提出SAM Audio Judge以解决音频分离中自动化感知评估的挑战

**关键词**：音频分离评估, 多模态感知指标, 无参考客观评估, 细粒度评估, 自动化评估系统

## 3 点简述
- 音频分离评估依赖主观测试或与感知不一致的客观指标，难以自动化扩展
- SAJ为多模态细粒度无参考客观指标，支持多领域和提示输入，覆盖四个评估维度
- 实验显示SAJ与人类感知高度对齐，并应用于数据过滤和模型重排序

## 摘要（原文）

> The performance evaluation remains a complex challenge in audio separation, and existing evaluation metrics are often misaligned with human perception, course-grained, relying on ground truth signals. On the other hand, subjective listening tests remain the gold standard for real-world evaluation, but they are expensive, time-consuming, and difficult to scale. This paper addresses the growing need for automated systems capable of evaluating audio separation without human intervention. The proposed evaluation metric, SAM Audio Judge (SAJ), is a multimodal fine-grained reference-free objective metric, which shows highly alignment with human perceptions. SAJ supports three audio domains (speech, music and general sound events) and three prompt inputs (text, visual and span), covering four different dimensions of evaluation (recall, percision, faithfulness, and overall). SAM Audio Judge also shows potential applications in data filtering, pseudo-labeling large datasets and reranking in audio separation models. We release our code and pre-trained models at: https://github.com/facebookresearch/sam-audio.

