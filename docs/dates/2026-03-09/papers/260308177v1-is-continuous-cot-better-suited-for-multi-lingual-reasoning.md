---
layout: default
title: Is continuous CoT better suited for multi-lingual reasoning?
---

# Is continuous CoT better suited for multi-lingual reasoning?
**arXiv**：[2603.08177v1](https://arxiv.org/abs/2603.08177) · [PDF](https://arxiv.org/pdf/2603.08177.pdf)  
**作者**：Ali Hamza Bashir, Behzad Shomali, Markus Frey, Mehdi Ali, Rafet Sifa, David Berghaus  

**一句话要点**：提出连续思维链方法以提升多语言推理的鲁棒性和效率

**关键词**：连续思维链, 多语言推理, 潜在空间表示, 零样本学习, 推理压缩, 跨语言鲁棒性

## 3 点简述
- 研究连续潜在空间推理是否增强多语言能力，对比连续思维链与标准监督微调
- 在英语、中文、德语、法语和乌尔都语上实验，连续推理在低资源语言和零样本设置中表现更优
- 方法压缩推理轨迹约29至50倍，显示连续表示具有语言不变性，可扩展跨语言推理

## 摘要（原文）

> We investigate whether performing reasoning in a continuous latent space leads to more robust multilingual capabilities. We compare Continuous Chain-of-Thought (using the CODI framework) against standard supervised fine-tuning across five typologically diverse languages: English, Chinese, German, French, and Urdu. Our experiments on GSM8k and CommonsenseQA demonstrate that continuous reasoning significantly outperforms explicit reasoning on low-resource languages, particularly in zero-shot settings where the target language was not seen during training. Additionally, this approach achieves extreme efficiency, compressing reasoning traces by approximately $29\times$ to $50\times$. These findings indicate that continuous latent representations naturally exhibit greater language invariance, offering a scalable solution for cross-lingual reasoning.

