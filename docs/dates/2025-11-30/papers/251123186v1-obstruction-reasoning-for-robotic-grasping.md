---
layout: default
title: Obstruction reasoning for robotic grasping
---

# Obstruction reasoning for robotic grasping
**arXiv**：[2511.23186v1](https://arxiv.org/abs/2511.23186) · [PDF](https://arxiv.org/pdf/2511.23186.pdf)  
**作者**：Runyu Jiao, Matteo Bortolon, Francesco Giuliari, Alice Fasoli, Sergio Povoli, Guofeng Mei, Yiming Wang, Fabio Poiesi  

**一句话要点**：提出UNOGrasp模型以解决机器人抓取中的遮挡推理问题

**关键词**：机器人抓取, 遮挡推理, 视觉语言模型, 多步推理, 强化学习

## 3 点简述
- 核心问题：现有视觉语言模型在遮挡推理和可达性规划方面存在局限
- 方法要点：基于遮挡路径的多步推理，结合监督与强化微调
- 实验或效果：在合成和真实环境中显著提升遮挡推理和抓取成功率

## 摘要（原文）

> Successful robotic grasping in cluttered environments not only requires a model to visually ground a target object but also to reason about obstructions that must be cleared beforehand. While current vision-language embodied reasoning models show emergent spatial understanding, they remain limited in terms of obstruction reasoning and accessibility planning. To bridge this gap, we present UNOGrasp, a learning-based vision-language model capable of performing visually-grounded obstruction reasoning to infer the sequence of actions needed to unobstruct the path and grasp the target object. We devise a novel multi-step reasoning process based on obstruction paths originated by the target object. We anchor each reasoning step with obstruction-aware visual cues to incentivize reasoning capability. UNOGrasp combines supervised and reinforcement finetuning through verifiable reasoning rewards. Moreover, we construct UNOBench, a large-scale dataset for both training and benchmarking, based on MetaGraspNetV2, with over 100k obstruction paths annotated by humans with obstruction ratios, contact points, and natural-language instructions. Extensive experiments and real-robot evaluations show that UNOGrasp significantly improves obstruction reasoning and grasp success across both synthetic and real-world environments, outperforming generalist and proprietary alternatives. Project website: https://tev-fbk.github.io/UnoGrasp/.

