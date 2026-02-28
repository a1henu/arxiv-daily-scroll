---
layout: default
title: Scaling Search Relevance: Augmenting App Store Ranking with LLM-Generated Judgments
---

# Scaling Search Relevance: Augmenting App Store Ranking with LLM-Generated Judgments
**arXiv**：[2602.23234v1](https://arxiv.org/abs/2602.23234) · [PDF](https://arxiv.org/pdf/2602.23234.pdf)  
**作者**：Evangelia Christakopoulou, Vivekkumar Patel, Hemanth Velaga, Sandip Gaikwad  

**一句话要点**：提出利用LLM生成文本相关性标签以增强应用商店搜索排序，解决专家标注稀缺问题。

**关键词**：搜索排序优化, LLM生成标签, 文本相关性, 行为相关性, 应用商店搜索, 离线评估

## 3 点简述
- 核心问题：商业搜索系统中文本相关性标签稀缺，而行为相关性标签丰富，影响排序优化。
- 方法要点：通过系统评估LLM配置，发现微调模型优于大型预训练模型，用于生成数百万文本相关性标签。
- 实验或效果：离线NDCG提升，线上A/B测试显示转化率显著增加，尤其在尾部查询中效果突出。

## 摘要（原文）

> Large-scale commercial search systems optimize for relevance to drive successful sessions that help users find what they are looking for. To maximize relevance, we leverage two complementary objectives: behavioral relevance (results users tend to click or download) and textual relevance (a result's semantic fit to the query). A persistent challenge is the scarcity of expert-provided textual relevance labels relative to abundant behavioral relevance labels. We first address this by systematically evaluating LLM configurations, finding that a specialized, fine-tuned model significantly outperforms a much larger pre-trained one in providing highly relevant labels. Using this optimal model as a force multiplier, we generate millions of textual relevance labels to overcome the data scarcity. We show that augmenting our production ranker with these textual relevance labels leads to a significant outward shift of the Pareto frontier: offline NDCG improves for behavioral relevance while simultaneously increasing for textual relevance. These offline gains were validated by a worldwide A/B test on the App Store ranker, which demonstrated a statistically significant +0.24% increase in conversion rate, with the most substantial performance gains occurring in tail queries, where the new textual relevance labels provide a robust signal in the absence of reliable behavioral relevance labels.

