---
layout: default
title: CoT-PL: Visual Chain-of-Thought Reasoning Meets Pseudo-Labeling for Open-Vocabulary Object Detection
---

# CoT-PL: Visual Chain-of-Thought Reasoning Meets Pseudo-Labeling for Open-Vocabulary Object Detection
**arXiv**：[2510.14792v1](https://arxiv.org/abs/2510.14792) · [PDF](https://arxiv.org/pdf/2510.14792.pdf)  
**作者**：Hojun Choi, Youngsun Lim, Jaeyo Shin, Hyunjung Shim  

**一句话要点**：提出CoT-PL框架，结合视觉链式推理与伪标注，提升拥挤或遮挡场景下的开放词汇目标检测鲁棒性。

**关键词**：开放词汇目标检测, 视觉链式推理, 伪标注, 对比背景学习, 特征解缠, 零样本推理

## 3 点简述
- 核心问题：现有开放词汇目标检测方法依赖直接图像-文本匹配，忽略中间推理步骤，在拥挤或遮挡场景中鲁棒性不足。
- 方法要点：引入视觉链式推理，分解对象理解为区域感知、类别识别和背景接地三步，并集成对比背景学习以增强特征解缠。
- 实验或效果：在开放词汇COCO和LVIS数据集上，新类检测性能显著提升，伪标注质量在拥挤和遮挡场景分别提高103.4%和168.4%。

## 摘要（原文）

> Open-vocabulary object detection (OVD) seeks to recognize and localize object
> categories beyond those seen during training. Recent approaches typically
> leverage vision-language models (VLMs) to generate pseudo-labels using
> image-text alignment, allowing detectors to generalize to unseen classes
> without explicit supervision. However, these methods depend heavily on direct
> image-text matching, neglecting the intermediate reasoning steps essential for
> interpreting semantically complex scenes. This results in limited robustness
> when confronted with crowded or occluded visual contexts. In this paper, we
> introduce CoT-PL, a new framework that employs structured visual
> chain-of-thought (CoT) reasoning into the pseudo-labeling process. CoT-PL
> decomposes object understanding into three interpretable steps: (1) region
> perception even for unseen objects, (2) category recognition via zero-shot
> reasoning, and (3) background grounding to separate semantically complex
> objects. Crucially, the third step naturally motivates our contrastive
> background learning (CBL) that uses the pre-computed background cues as
> negatives to promote feature disentanglement between objects and background. In
> this way, CoT reasoning and CBL form an integrated pipeline tailored to robust
> pseudo-labeling in crowded or occluded scenes. Notably, in these two settings,
> our novel-class pseudo-label quality achieves relative improvements of 103.4%
> and 168.4% over the best prior, respectively. Our extensive experiments
> demonstrate that CoT-PL achieves +7.7 AP50 on open-vocabulary COCO and +2.9
> mask AP on LVIS for novel classes, setting a new state of the art.

