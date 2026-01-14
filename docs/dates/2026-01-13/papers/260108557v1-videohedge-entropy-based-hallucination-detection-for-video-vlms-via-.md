---
layout: default
title: VideoHEDGE: Entropy-Based Hallucination Detection for Video-VLMs via Semantic Clustering and Spatiotemporal Perturbations
---

# VideoHEDGE: Entropy-Based Hallucination Detection for Video-VLMs via Semantic Clustering and Spatiotemporal Perturbations
**arXiv**：[2601.08557v1](https://arxiv.org/abs/2601.08557) · [PDF](https://arxiv.org/pdf/2601.08557.pdf)  
**作者**：Sushant Gautam, Cise Midoglu, Vajira Thambawita, Michael A. Riegler, Pål Halvorsen  

**一句话要点**：提出VideoHEDGE框架，通过语义聚类和时空扰动检测视频视觉语言模型的幻觉问题。

**关键词**：视频视觉语言模型, 幻觉检测, 语义熵, 时空扰动, 视频问答, 可靠性评估

## 3 点简述
- 视频视觉语言模型在视频问答中常产生高置信度幻觉，现有不确定性指标与正确性不匹配。
- VideoHEDGE扩展基于熵的可靠性估计，结合语义聚类和时空扰动生成多个答案变体。
- 在SoccerChat基准上，VASE得分在三个7B模型上实现最高ROC-AUC，嵌入聚类性能接近NLI但计算成本更低。

## 摘要（原文）

> Hallucinations in video-capable vision-language models (Video-VLMs) remain frequent and high-confidence, while existing uncertainty metrics often fail to align with correctness. We introduce VideoHEDGE, a modular framework for hallucination detection in video question answering that extends entropy-based reliability estimation from images to temporally structured inputs. Given a video-question pair, VideoHEDGE draws a baseline answer and multiple high-temperature generations from both clean clips and photometrically and spatiotemporally perturbed variants, then clusters the resulting textual outputs into semantic hypotheses using either Natural Language Inference (NLI)-based or embedding-based methods. Cluster-level probability masses yield three reliability scores: Semantic Entropy (SE), RadFlag, and Vision-Amplified Semantic Entropy (VASE). We evaluate VideoHEDGE on the SoccerChat benchmark using an LLM-as-a-judge to obtain binary hallucination labels. Across three 7B Video-VLMs (Qwen2-VL, Qwen2.5-VL, and a SoccerChat-finetuned model), VASE consistently achieves the highest ROC-AUC, especially at larger distortion budgets, while SE and RadFlag often operate near chance. We further show that embedding-based clustering matches NLI-based clustering in detection performance at substantially lower computational cost, and that domain fine-tuning reduces hallucination frequency but yields only modest improvements in calibration. The hedge-bench PyPI library enables reproducible and extensible benchmarking, with full code and experimental resources available at https://github.com/Simula/HEDGE#videohedge .

