---
layout: default
title: VeriSciQA: An Auto-Verified Dataset for Scientific Visual Question Answering
---

# VeriSciQA: An Auto-Verified Dataset for Scientific Visual Question Answering
**arXiv**：[2511.19899v1](https://arxiv.org/abs/2511.19899) · [PDF](https://arxiv.org/pdf/2511.19899.pdf)  
**作者**：Yuyi Li, Daoyuan Chen, Zhen Wang, Yutong Lu, Yaliang Li  

**一句话要点**：提出VeriSciQA数据集以解决科学视觉问答中数据质量不足的问题

**关键词**：科学视觉问答, 数据集构建, 跨模态验证, 视觉语言模型, 开源基准

## 3 点简述
- 科学视觉问答缺乏高质量公开数据集，阻碍开源模型发展
- 采用生成-验证框架，结合跨模态一致性检查过滤错误QA对
- 实验显示VeriSciQA提升模型性能，人类评估验证其正确性

## 摘要（原文）

> Large Vision-Language Models (LVLMs) show promise for scientific applications, yet open-source models still struggle with Scientific Visual Question Answering (SVQA), namely answering questions about figures from scientific papers. A key bottleneck lies in the lack of public, large-scale, high-quality SVQA datasets. Although recent work uses LVLMs to synthesize data at scale, we identify systematic errors in their resulting QA pairs, stemming from LVLMs' inherent limitations and information asymmetry between figures and text. To address these challenges, we propose a verification-centric Generate-then-Verify framework that first generates QA pairs with figure-associated textual context, then applies cross-modal consistency checks against figures along with auxiliary filters to eliminate erroneous pairs. We instantiate this framework to curate VeriSciQA, a dataset of 20,351 QA pairs spanning 20 scientific domains and 12 figure types. VeriSciQA poses a challenging benchmark for open-source models, with a substantial accuracy gap between the leading open-source models (64%) and a proprietary model (82%). Moreover, models fine-tuned on VeriSciQA achieve consistent improvements on SVQA benchmarks, with performance gains that scale with data size and surpass models trained on existing datasets. Human evaluation further validates the superior correctness of VeriSciQA. Together, these evidences demonstrate that continued data expansion by our scalable framework can further advance SVQA capability in the open-source community.

