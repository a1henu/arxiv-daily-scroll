---
layout: default
title: SONIC-O1: A Real-World Benchmark for Evaluating Multimodal Large Language Models on Audio-Video Understanding
---

# SONIC-O1: A Real-World Benchmark for Evaluating Multimodal Large Language Models on Audio-Video Understanding
**arXiv**：[2601.21666v1](https://arxiv.org/abs/2601.21666) · [PDF](https://arxiv.org/pdf/2601.21666.pdf)  
**作者**：Ahmed Y. Radwan, Christos Emmanouilidis, Hina Tabassum, Deval Pandya, Shaina Raza  

**一句话要点**：提出SONIC-O1基准以评估多模态大语言模型在真实世界音视频理解中的性能

**关键词**：音视频理解, 多模态大语言模型, 基准评估, 时序定位, 人口统计偏差, 真实世界数据

## 3 点简述
- 现有MLLM研究多关注静态图像，音视频序列理解评估不足
- SONIC-O1包含13个对话领域、4958条人工验证标注，支持摘要、多选问答和时序定位任务
- 实验显示开源与闭源模型在时序定位上性能差距显著，且存在人口统计群体间差异

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) are a major focus of recent AI research. However, most prior work focuses on static image understanding, while their ability to process sequential audio-video data remains underexplored. This gap highlights the need for a high-quality benchmark to systematically evaluate MLLM performance in a real-world setting. We introduce SONIC-O1, a comprehensive, fully human-verified benchmark spanning 13 real-world conversational domains with 4,958 annotations and demographic metadata. SONIC-O1 evaluates MLLMs on key tasks, including open-ended summarization, multiple-choice question (MCQ) answering, and temporal localization with supporting rationales (reasoning). Experiments on closed- and open-source models reveal limitations. While the performance gap in MCQ accuracy between two model families is relatively small, we observe a substantial 22.6% performance difference in temporal localization between the best performing closed-source and open-source models. Performance further degrades across demographic groups, indicating persistent disparities in model behavior. Overall, SONIC-O1 provides an open evaluation suite for temporally grounded and socially robust multimodal understanding. We release SONIC-O1 for reproducibility and research: Project page: https://vectorinstitute.github.io/sonic-o1/ Dataset: https://huggingface.co/datasets/vector-institute/sonic-o1 Github: https://github.com/vectorinstitute/sonic-o1 Leaderboard: https://huggingface.co/spaces/vector-institute/sonic-o1-leaderboard

