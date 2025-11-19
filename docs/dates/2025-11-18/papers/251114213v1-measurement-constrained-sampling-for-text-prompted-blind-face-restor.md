---
layout: default
title: Measurement-Constrained Sampling for Text-Prompted Blind Face Restoration
---

# Measurement-Constrained Sampling for Text-Prompted Blind Face Restoration
**arXiv**：[2511.14213v1](https://arxiv.org/abs/2511.14213) · [PDF](https://arxiv.org/pdf/2511.14213.pdf)  
**作者**：Wenjie Li, Yulun Zhang, Guangwei Gao, Heng Guo, Zhanyu Ma  

**一句话要点**：提出测量约束采样方法，实现文本提示的盲人脸多样化恢复

**关键词**：盲人脸恢复, 文本提示生成, 测量约束采样, 扩散模型, 逆问题求解

## 3 点简述
- 盲人脸恢复存在一对多问题，现有方法难以生成多样化结果
- 通过构建逆问题，结合前向和后向测量约束，实现文本引导的扩散采样
- 实验显示方法能生成与提示对齐的结果，优于现有盲人脸恢复方法

## 摘要（原文）

> Blind face restoration (BFR) may correspond to multiple plausible high-quality (HQ) reconstructions under extremely low-quality (LQ) inputs. However, existing methods typically produce deterministic results, struggling to capture this one-to-many nature. In this paper, we propose a Measurement-Constrained Sampling (MCS) approach that enables diverse LQ face reconstructions conditioned on different textual prompts. Specifically, we formulate BFR as a measurement-constrained generative task by constructing an inverse problem through controlled degradations of coarse restorations, which allows posterior-guided sampling within text-to-image diffusion. Measurement constraints include both Forward Measurement, which ensures results align with input structures, and Reverse Measurement, which produces projection spaces, ensuring that the solution can align with various prompts. Experiments show that our MCS can generate prompt-aligned results and outperforms existing BFR methods. Codes will be released after acceptance.

