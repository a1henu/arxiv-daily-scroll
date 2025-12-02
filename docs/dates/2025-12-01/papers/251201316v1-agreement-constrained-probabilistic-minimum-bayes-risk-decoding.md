---
layout: default
title: Agreement-Constrained Probabilistic Minimum Bayes Risk Decoding
---

# Agreement-Constrained Probabilistic Minimum Bayes Risk Decoding
**arXiv**：[2512.01316v1](https://arxiv.org/abs/2512.01316) · [PDF](https://arxiv.org/pdf/2512.01316.pdf)  
**作者**：Koki Natsumi, Hiroyuki Deguchi, Yusuke Sakai, Hidetaka Kamigaito, Taro Watanabe  

**一句话要点**：提出基于一致性约束的概率最小贝叶斯风险解码，以在机器翻译中平衡质量与计算成本。

**关键词**：机器翻译, 最小贝叶斯风险解码, 矩阵补全, 知识蒸馏, 计算效率优化

## 3 点简述
- 最小贝叶斯风险解码计算成本高，需评估候选集所有成对分数，导致二次时间开销。
- 概率最小贝叶斯风险解码通过采样和矩阵补全减少计算，但质量随调用次数减少而下降。
- 新方法利用知识蒸馏模型指导矩阵补全，在WMT'23任务中提升近似误差和翻译质量。

## 摘要（原文）

> Minimum Bayes risk (MBR) decoding generates high-quality translations by maximizing the expected utility of output candidates, but it evaluates all pairwise scores over the candidate set; hence, it takes quadratic time with respect to the number of candidates. To reduce the number of utility function calls, probabilistic MBR (PMBR) decoding partially evaluates quality scores using sampled pairs of candidates and completes the missing scores with a matrix completion algorithm. Nevertheless, it degrades the translation quality as the number of utility function calls is reduced. Therefore, to improve the trade-off between quality and cost, we propose agreement-constrained PMBR (AC-PMBR) decoding, which leverages a knowledge distilled model to guide the completion of the score matrix. Our AC-PMBR decoding improved approximation errors of matrix completion by up to 3 times and achieved higher translation quality compared with PMBR decoding at a comparable computational cost on the WMT'23 En$\leftrightarrow$De translation tasks.

