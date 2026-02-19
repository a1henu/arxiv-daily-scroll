---
layout: default
title: Factorization Machine with Quadratic-Optimization Annealing for RNA Inverse Folding and Evaluation of Binary-Integer Encoding and Nucleotide Assignment
---

# Factorization Machine with Quadratic-Optimization Annealing for RNA Inverse Folding and Evaluation of Binary-Integer Encoding and Nucleotide Assignment
**arXiv**：[2602.16643v1](https://arxiv.org/abs/2602.16643) · [PDF](https://arxiv.org/pdf/2602.16643.pdf)  
**作者**：Shuta Kikuchi, Shu Tanaka  

**一句话要点**：提出基于二次优化退火的因子分解机方法，用于RNA逆折叠问题，并评估编码与分配策略的影响。

**关键词**：RNA逆折叠, 因子分解机, 二次优化退火, 二进制编码, 核苷酸分配, 黑盒优化

## 3 点简述
- RNA逆折叠问题旨在寻找能优先形成目标二级结构的核苷酸序列，现有方法常需大量序列评估，限制了成本高昂实验的应用。
- 本研究采用因子分解机结合二次优化退火方法，这是一种离散黑盒优化技术，能在有限评估次数内获得高质量解。
- 实验评估了24种核苷酸到整数分配与四种二进制编码方法的组合，发现独热和畴壁编码在归一化集成缺陷值上表现更优，特定分配能促进茎区富集，提高热力学稳定性。

## 摘要（原文）

> The RNA inverse folding problem aims to identify nucleotide sequences that preferentially adopt a given target secondary structure. While various heuristic and machine learning-based approaches have been proposed, many require a large number of sequence evaluations, which limits their applicability when experimental validation is costly. We propose a method to solve the problem using a factorization machine with quadratic-optimization annealing (FMQA). FMQA is a discrete black-box optimization method reported to obtain high-quality solutions with a limited number of evaluations. Applying FMQA to the problem requires converting nucleotides into binary variables. However, the influence of integer-to-nucleotide assignments and binary-integer encoding on the performance of FMQA has not been thoroughly investigated, even though such choices determine the structure of the surrogate model and the search landscape, and thus can directly affect solution quality. Therefore, this study aims both to establish a novel FMQA framework for RNA inverse folding and to analyze the effects of these assignments and encoding methods. We evaluated all 24 possible assignments of the four nucleotides to the ordered integers (0-3), in combination with four binary-integer encoding methods. Our results demonstrated that one-hot and domain-wall encodings outperform binary and unary encodings in terms of the normalized ensemble defect value. In domain-wall encoding, nucleotides assigned to the boundary integers (0 and 3) appeared with higher frequency. In the RNA inverse folding problem, assigning guanine and cytosine to these boundary integers promoted their enrichment in stem regions, which led to more thermodynamically stable secondary structures than those obtained with one-hot encoding.

