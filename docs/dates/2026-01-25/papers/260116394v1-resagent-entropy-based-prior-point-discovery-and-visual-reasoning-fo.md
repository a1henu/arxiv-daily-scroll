---
layout: default
title: ResAgent: Entropy-based Prior Point Discovery and Visual Reasoning for Referring Expression Segmentation
---

# ResAgent: Entropy-based Prior Point Discovery and Visual Reasoning for Referring Expression Segmentation
**arXiv**：[2601.16394v1](https://arxiv.org/abs/2601.16394) · [PDF](https://arxiv.org/pdf/2601.16394.pdf)  
**作者**：Yihao Wang, Jusheng Zhang, Ziyi Tang, Keze Wang, Meng Yang  

**一句话要点**：提出ResAgent框架，通过熵基点发现和视觉推理解决指代表达分割中的点提示冗余和文本坐标不可靠问题。

**关键词**：指代表达分割, 熵基点发现, 视觉推理, 多模态大语言模型, 语义分割, 视觉语言对齐

## 3 点简述
- 核心问题：现有方法依赖MLLM的粗边界框导致点提示冗余，且文本坐标推理无法区分视觉相似干扰物。
- 方法要点：引入熵基点发现（EBD）建模空间不确定性选择高信息点，结合视觉推理（VBR）通过视觉语义对齐验证点正确性。
- 实验或效果：在RefCOCO等四个基准数据集上实现新SOTA，验证了框架在最小提示下生成准确语义分割掩码的有效性。

## 摘要（原文）

> Referring Expression Segmentation (RES) is a core vision-language segmentation task that enables pixel-level understanding of targets via free-form linguistic expressions, supporting critical applications such as human-robot interaction and augmented reality. Despite the progress of Multimodal Large Language Model (MLLM)-based approaches, existing RES methods still suffer from two key limitations: first, the coarse bounding boxes from MLLMs lead to redundant or non-discriminative point prompts; second, the prevalent reliance on textual coordinate reasoning is unreliable, as it fails to distinguish targets from visually similar distractors. To address these issues, we propose \textbf{\model}, a novel RES framework integrating \textbf{E}ntropy-\textbf{B}ased Point \textbf{D}iscovery (\textbf{EBD}) and \textbf{V}ision-\textbf{B}ased \textbf{R}easoning (\textbf{VBR}). Specifically, EBD identifies high-information candidate points by modeling spatial uncertainty within coarse bounding boxes, treating point selection as an information maximization process. VBR verifies point correctness through joint visual-semantic alignment, abandoning text-only coordinate inference for more robust validation. Built on these components, \model implements a coarse-to-fine workflow: bounding box initialization, entropy-guided point discovery, vision-based validation, and mask decoding. Extensive evaluations on four benchmark datasets (RefCOCO, RefCOCO+, RefCOCOg, and ReasonSeg) demonstrate that \model achieves new state-of-the-art performance across all four benchmarks, highlighting its effectiveness in generating accurate and semantically grounded segmentation masks with minimal prompts.

