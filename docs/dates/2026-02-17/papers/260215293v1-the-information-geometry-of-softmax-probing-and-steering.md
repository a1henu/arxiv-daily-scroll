---
layout: default
title: The Information Geometry of Softmax: Probing and Steering
---

# The Information Geometry of Softmax: Probing and Steering
**arXiv**：[2602.15293v1](https://arxiv.org/abs/2602.15293) · [PDF](https://arxiv.org/pdf/2602.15293.pdf)  
**作者**：Kiho Park, Todd Nief, Yo Joong Choe, Victor Veitch  

**一句话要点**：提出双引导方法，利用信息几何优化软max表示空间的概念操控

**关键词**：信息几何, 软max表示, 线性表示假设, 概念操控, 双引导方法

## 3 点简述
- 核心问题：AI系统如何将语义结构编码到表示空间的几何结构中
- 方法要点：基于信息几何理论，开发双引导方法以线性探针稳健引导概念表示
- 实验或效果：双引导增强概念操控的可控性和稳定性，最小化非目标概念变化

## 摘要（原文）

> This paper concerns the question of how AI systems encode semantic structure into the geometric structure of their representation spaces. The motivating observation of this paper is that the natural geometry of these representation spaces should reflect the way models use representations to produce behavior. We focus on the important special case of representations that define softmax distributions. In this case, we argue that the natural geometry is information geometry. Our focus is on the role of information geometry on semantic encoding and the linear representation hypothesis. As an illustrative application, we develop "dual steering", a method for robustly steering representations to exhibit a particular concept using linear probes. We prove that dual steering optimally modifies the target concept while minimizing changes to off-target concepts. Empirically, we find that dual steering enhances the controllability and stability of concept manipulation.

