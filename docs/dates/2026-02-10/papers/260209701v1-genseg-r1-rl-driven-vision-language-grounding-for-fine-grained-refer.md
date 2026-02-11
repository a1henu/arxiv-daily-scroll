---
layout: default
title: GenSeg-R1: RL-Driven Vision-Language Grounding for Fine-Grained Referring Segmentation
---

# GenSeg-R1: RL-Driven Vision-Language Grounding for Fine-Grained Referring Segmentation
**arXiv**：[2602.09701v1](https://arxiv.org/abs/2602.09701) · [PDF](https://arxiv.org/pdf/2602.09701.pdf)  
**作者**：Sandesh Hegde, Jaison Saji Chacko, Debarshi Banerjee, Uma Mahesh  

**一句话要点**：提出GenSeg-R1框架，通过强化学习驱动视觉语言模型进行细粒度指代分割

**关键词**：细粒度指代分割, 视觉语言模型, 强化学习, 结构化空间提示, 无监督微调, SAM 2

## 3 点简述
- 研究细粒度指代图像分割，采用解耦的推理-分割流程，无需监督推理链标注
- 使用Group Relative Policy Optimization微调Qwen3-VL模型，生成结构化空间提示以引导分割
- 在RefCOCOg和GRefCOCO数据集上显著超越基线模型，提升分割质量和负提示检测能力

## 摘要（原文）

> We study fine-grained referring image segmentation via a decoupled reason-then-segment pipeline. A vision-language model (VLM) receives an image and a natural-language query, reasons about the scene, and emits structured spatial prompts: a bounding box plus two interior keypoints for every referred instance. A frozen promptable segmenter (SAM 2) converts these prompts into high-quality masks.
>   Within our GenSeg-R1 framework we finetune Qwen3-VL models (4B and 8B parameters) using Group Relative Policy Optimization (GRPO), requiring no supervised reasoning-chain annotations. On RefCOCOg validation our best model (GenSeg-R1-8B) achieves 0.7127 cIoU and 0.7382 mIoU, substantially outperforming the corresponding Qwen3-VL Instruct baselines (+15.3 and +21.9 points, respectively) and surpassing Seg-Zero-7B [3] by +3.3 cIoU under identical evaluation.
>   We further introduce GenSeg-R1-G, a variant trained on GRefCOCO [9] with a SAM 2 in-the-loop reward that directly optimizes mask quality. On GRefCOCO validation GenSeg-R1-G achieves 76.69% target mIoU with 82.40% accuracy on negative (no-target) prompts, substantially outperforming Seg-R1-7B and Seg-Zero-7B, which lack no-target detection capability. On ReasonSeg test, GenSeg-R1-4B reaches 68.40% mIoU, surpassing Seg-Zero-7B by +7.0 and Seg-R1-7B by +10.7 points.

