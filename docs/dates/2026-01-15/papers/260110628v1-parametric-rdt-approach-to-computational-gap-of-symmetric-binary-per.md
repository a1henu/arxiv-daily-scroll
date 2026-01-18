---
layout: default
title: Parametric RDT approach to computational gap of symmetric binary perceptron
---

# Parametric RDT approach to computational gap of symmetric binary perceptron
**arXiv**：[2601.10628v1](https://arxiv.org/abs/2601.10628) · [PDF](https://arxiv.org/pdf/2601.10628.pdf)  
**作者**：Mihailo Stojnic  

**一句话要点**：提出参数化RDT方法探究对称二元感知机的统计-计算间隙

**关键词**：对称二元感知机, 统计-计算间隙, 随机对偶理论, 约束密度阈值, 算法性能, 参数化分析

## 3 点简述
- 研究对称二元感知机中统计-计算间隙的存在性
- 利用参数化全提升随机对偶理论分析约束密度阈值变化
- 理论预测与文献结果一致，并设计算法验证性能

## 摘要（原文）

> We study potential presence of statistical-computational gaps (SCG) in symmetric binary perceptrons (SBP) via a parametric utilization of \emph{fully lifted random duality theory} (fl-RDT) [96]. A structural change from decreasingly to arbitrarily ordered $c$-sequence (a key fl-RDT parametric component) is observed on the second lifting level and associated with \emph{satisfiability} ($α_c$) -- \emph{algorithmic} ($α_a$) constraints density threshold change thereby suggesting a potential existence of a nonzero computational gap $SCG=α_c-α_a$. The second level estimate is shown to match the theoretical $α_c$ whereas the $r\rightarrow \infty$ level one is proposed to correspond to $α_a$. For example, for the canonical SBP ($κ=1$ margin) we obtain $α_c\approx 1.8159$ on the second and $α_a\approx 1.6021$ (with converging tendency towards $\sim 1.59$ range) on the seventh level. Our propositions remarkably well concur with recent literature: (i) in [20] local entropy replica approach predicts $α_{LE}\approx 1.58$ as the onset of clustering defragmentation (presumed driving force behind locally improving algorithms failures); (ii) in $α\rightarrow 0$ regime we obtain on the third lifting level $κ\approx 1.2385\sqrt{\frac{α_a}{-\log\left ( α_a \right ) }}$ which qualitatively matches overlap gap property (OGP) based predictions of [43] and identically matches local entropy based predictions of [24]; (iii) $c$-sequence ordering change phenomenology mirrors the one observed in asymmetric binary perceptron (ABP) in [98] and the negative Hopfield model in [100]; and (iv) as in [98,100], we here design a CLuP based algorithm whose practical performance closely matches proposed theoretical predictions.

