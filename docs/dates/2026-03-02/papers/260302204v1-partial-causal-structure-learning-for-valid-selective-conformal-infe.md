---
layout: default
title: Partial Causal Structure Learning for Valid Selective Conformal Inference under Interventions
---

# Partial Causal Structure Learning for Valid Selective Conformal Inference under Interventions
**arXiv**：[2603.02204v1](https://arxiv.org/abs/2603.02204) · [PDF](https://arxiv.org/pdf/2603.02204.pdf)  
**作者**：Amir Asiaee, Kavey Aryan, James P. Long  

**一句话要点**：提出部分因果结构学习方法，用于干预下有效选择性共形推断

**关键词**：选择性共形推断, 因果结构学习, 干预分析, 鲁棒校准, 基因组扰动实验

## 3 点简述
- 研究干预场景中未知因果结构下选择性共形推断的校准问题
- 提出污染鲁棒的覆盖定理和任务驱动的部分因果学习框架
- 在合成和真实基因组数据上验证方法保持覆盖率并控制污染

## 摘要（原文）

> Selective conformal prediction can yield substantially tighter uncertainty sets when we can identify calibration examples that are exchangeable with the test example. In interventional settings, such as perturbation experiments in genomics, exchangeability often holds only within subsets of interventions that leave a target variable "unaffected" (e.g., non-descendants of an intervened node in a causal graph). We study the practical regime where this invariance structure is unknown and must be learned from data. Our contributions are: (i) a contamination-robust conformal coverage theorem that quantifies how misclassification of "unaffected" calibration examples degrades coverage via an explicit function $g(δ,n)$ of the contamination fraction and calibration set size, providing a finite-sample lower bound that holds for arbitrary contaminating distributions; (ii) a task-driven partial causal learning formulation that estimates only the binary descendant indicators $Z_{a,i}=\mathbf{1}\{i\in\mathrm{desc}(a)\}$ needed for selective calibration, rather than the full causal graph; and (iii) algorithms for descendant discovery via perturbation intersection patterns (differentially affected variable set intersections across interventions), and for approximate distance-to-intervention estimation via local invariant causal prediction. We provide recovery conditions under which contamination is controlled. Experiments on synthetic linear structural equation models (SEMs) validate the bound: under controlled contamination up to $δ=0.30$, the corrected procedure maintains $\ge 0.95$ coverage while uncorrected selective CP degrades to $0.867$. A proof-of-concept on Replogle K562 CRISPR interference (CRISPRi) perturbation data demonstrates applicability to real genomic screens.

