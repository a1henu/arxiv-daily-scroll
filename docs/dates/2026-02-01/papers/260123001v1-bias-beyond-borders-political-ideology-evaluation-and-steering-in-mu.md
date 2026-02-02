---
layout: default
title: Bias Beyond Borders: Political Ideology Evaluation and Steering in Multilingual LLMs
---

# Bias Beyond Borders: Political Ideology Evaluation and Steering in Multilingual LLMs
**arXiv**：[2601.23001v1](https://arxiv.org/abs/2601.23001) · [PDF](https://arxiv.org/pdf/2601.23001.pdf)  
**作者**：Afrozah Nadeem, Agrima, Mehwish Nasim, Usman Naseem  

**一句话要点**：提出跨语言对齐引导框架以评估和缓解多语言大语言模型的政治偏见

**关键词**：政治偏见评估, 跨语言对齐, 后处理缓解, 多语言大语言模型, 意识形态表示, 公平性治理

## 3 点简述
- 评估50个国家33种语言的政治偏见，揭示跨语言一致性问题
- 提出跨语言对齐引导方法，对齐意识形态表示并动态调节干预强度
- 实验显示偏见显著减少，响应质量下降最小，平衡中立性与多样性

## 摘要（原文）

> Large Language Models (LLMs) increasingly shape global discourse, making fairness and ideological neutrality essential for responsible AI deployment. Despite growing attention to political bias in LLMs, prior work largely focuses on high-resource, Western languages or narrow multilingual settings, leaving cross-lingual consistency and safe post-hoc mitigation underexplored. To address this gap, we present a large-scale multilingual evaluation of political bias spanning 50 countries and 33 languages. We introduce a complementary post-hoc mitigation framework, Cross-Lingual Alignment Steering (CLAS), designed to augment existing steering methods by aligning ideological representations across languages and dynamically regulating intervention strength. This method aligns latent ideological representations induced by political prompts into a shared ideological subspace, ensuring cross lingual consistency, with the adaptive mechanism prevents over correction and preserves coherence. Experiments demonstrate substantial bias reduction along both economic and social axes with minimal degradation in response quality. The proposed framework establishes a scalable and interpretable paradigm for fairness-aware multilingual LLM governance, balancing ideological neutrality with linguistic and cultural diversity.

