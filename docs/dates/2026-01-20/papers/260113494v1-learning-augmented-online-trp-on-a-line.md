---
layout: default
title: Learning-Augmented Online TRP on a Line
---

# Learning-Augmented Online TRP on a Line
**arXiv**：[2601.13494v1](https://arxiv.org/abs/2601.13494) · [PDF](https://arxiv.org/pdf/2601.13494.pdf)  
**作者**：Swapnil Guragain, Gokarna Sharma  

**一句话要点**：提出学习增强在线旅行修理工问题在线算法，结合预测优化完成时间。

**关键词**：在线算法, 旅行修理工问题, 学习增强框架, 竞争分析, 预测模型, 确定性算法

## 3 点简述
- 研究在线旅行修理工问题在线版本，目标最小化请求完成时间总和。
- 设计确定性算法，完美预测时竞争比约3.732，不完美时竞争比受误差影响。
- 建立3竞争比下界，扩展至原始模型，为学习增强框架首次结果。

## 摘要（原文）

> We study the online traveling repairperson problem on a line within the recently proposed learning-augmented framework, which provides predictions on the requests to be served via machine learning. In the original model (with no predictions), there is a stream of requests released over time along the line. The goal is to minimize the sum (or average) of the completion times of the requests. In the original model, the state-of-the-art competitive ratio lower bound is $1+\sqrt{2} > 2.414$ for any deterministic algorithm and the state-of-the-art competitive ratio upper bound is 4 for a deterministic algorithm. Our prediction model involves predicted positions, possibly error-prone, of each request in the stream known a priori but the arrival times of requests are not known until their arrival. We first establish a 3-competitive lower bound which extends to the original model. We then design a deterministic algorithm that is $(2+\sqrt{3})\approx 3.732$-competitive when predictions are perfect. With imperfect predictions (maximum error $δ> 0$), we show that our deterministic algorithm becomes $\min\{3.732+4δ,4\}$-competitive, knowing $δ$. To the best of our knowledge, these are the first results for online traveling repairperson problem in the learning-augmented framework.

