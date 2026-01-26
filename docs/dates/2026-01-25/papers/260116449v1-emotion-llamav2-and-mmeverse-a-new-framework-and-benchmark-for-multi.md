---
layout: default
title: Emotion-LLaMAv2 and MMEVerse: A New Framework and Benchmark for Multimodal Emotion Understanding
---

# Emotion-LLaMAv2 and MMEVerse: A New Framework and Benchmark for Multimodal Emotion Understanding
**arXiv**：[2601.16449v1](https://arxiv.org/abs/2601.16449) · [PDF](https://arxiv.org/pdf/2601.16449.pdf)  
**作者**：Xiaojiang Peng, Jingyi Chen, Zebang Cheng, Bao Peng, Fengyi Wu, Yifei Dong, Shuyuan Tu, Qiyu Hu, Huiting Huang, Yuxiang Lin, Jun-Yan He, Kai Wang, Zheng Lian, Zhi-Qi Cheng  

**一句话要点**：提出Emotion-LLaMAv2框架与MMEVerse基准，用于解决多模态情感理解中的模型能力不足与评估标准化问题

**关键词**：多模态情感理解, 指令调优, 端到端学习, 情感推理, 基准数据集, 多模态融合

## 3 点简述
- 多模态大语言模型在情感推理方面能力有限，且领域缺乏高质量标注数据集和标准化评估基准
- Emotion-LLaMAv2引入端到端多视角编码器、Conv Attention预融合模块和感知到认知课程指令调优方案
- MMEVerse整合12个公开数据集并重新标注，提供13万训练样本和3.6万测试样本的标准化评估环境

## 摘要（原文）

> Understanding human emotions from multimodal signals poses a significant challenge in affective computing and human-robot interaction. While multimodal large language models (MLLMs) have excelled in general vision-language tasks, their capabilities in emotional reasoning remain limited. The field currently suffers from a scarcity of large-scale datasets with high-quality, descriptive emotion annotations and lacks standardized benchmarks for evaluation. Our preliminary framework, Emotion-LLaMA, pioneered instruction-tuned multimodal learning for emotion reasoning but was restricted by explicit face detectors, implicit fusion strategies, and low-quality training data with limited scale. To address these limitations, we present Emotion-LLaMAv2 and the MMEVerse benchmark, establishing an end-to-end pipeline together with a standardized evaluation setting for emotion recognition and reasoning. Emotion-LLaMAv2 introduces three key advances. First, an end-to-end multiview encoder eliminates external face detection and captures nuanced emotional cues via richer spatial and temporal multiview tokens. Second, a Conv Attention pre-fusion module is designed to enable simultaneous local and global multimodal feature interactions external to the LLM backbone. Third, a perception-to-cognition curriculum instruction tuning scheme within the LLaMA2 backbone unifies emotion recognition and free-form emotion reasoning. To support large-scale training and reproducible evaluation, MMEVerse aggregates twelve publicly available emotion datasets, including IEMOCAP, MELD, DFEW, and MAFW, into a unified multimodal instruction format. The data are re-annotated via a multi-agent pipeline involving Qwen2 Audio, Qwen2.5 VL, and GPT 4o, producing 130k training clips and 36k testing clips across 18 evaluation benchmarks.

