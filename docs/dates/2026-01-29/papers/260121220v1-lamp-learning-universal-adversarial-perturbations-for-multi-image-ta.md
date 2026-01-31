---
layout: default
title: LAMP: Learning Universal Adversarial Perturbations for Multi-Image Tasks via Pre-trained Models
---

# LAMP: Learning Universal Adversarial Perturbations for Multi-Image Tasks via Pre-trained Models
**arXiv**：[2601.21220v1](https://arxiv.org/abs/2601.21220) · [PDF](https://arxiv.org/pdf/2601.21220.pdf)  
**作者**：Alvi Md Ishmam, Najibul Haque Sarker, Zaber Ibn Abdul Hakim, Chris Thomas  

**一句话要点**：提出LAMP方法以解决多图像多模态大语言模型的黑盒对抗攻击问题

**关键词**：多模态大语言模型, 对抗攻击, 黑盒攻击, 通用对抗扰动, 多图像任务, 注意力机制

## 3 点简述
- 核心问题：多图像多模态大语言模型在对抗攻击下的脆弱性未知，现有攻击多为单图像白盒模型，不实用
- 方法要点：LAMP采用基于注意力的约束和跨图像传染约束，学习通用对抗扰动，无需修改所有输入
- 实验或效果：LAMP在多个视觉语言任务和模型上超越现有方法，达到最高攻击成功率

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have achieved remarkable performance across vision-language tasks. Recent advancements allow these models to process multiple images as inputs. However, the vulnerabilities of multi-image MLLMs remain unexplored. Existing adversarial attacks focus on single-image settings and often assume a white-box threat model, which is impractical in many real-world scenarios. This paper introduces LAMP, a black-box method for learning Universal Adversarial Perturbations (UAPs) targeting multi-image MLLMs. LAMP applies an attention-based constraint that prevents the model from effectively aggregating information across images. LAMP also introduces a novel cross-image contagious constraint that forces perturbed tokens to influence clean tokens, spreading adversarial effects without requiring all inputs to be modified. Additionally, an index-attention suppression loss enables a robust position-invariant attack. Experimental results show that LAMP outperforms SOTA baselines and achieves the highest attack success rates across multiple vision-language tasks and models.

