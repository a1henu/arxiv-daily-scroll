---
layout: default
title: GI-Bench: A Panoramic Benchmark Revealing the Knowledge-Experience Dissociation of Multimodal Large Language Models in Gastrointestinal Endoscopy Against Clinical Standards
---

# GI-Bench: A Panoramic Benchmark Revealing the Knowledge-Experience Dissociation of Multimodal Large Language Models in Gastrointestinal Endoscopy Against Clinical Standards
**arXiv**：[2601.08183v1](https://arxiv.org/abs/2601.08183) · [PDF](https://arxiv.org/pdf/2601.08183.pdf)  
**作者**：Yan Zhu, Te Luo, Pei-Yao Fu, Zhen Zhang, Zi-Long Wang, Yi-Fan Qu, Zi-Han Geng, Jia-Qi Xu, Lu Yao, Li-Yun Ma, Wei Su, Wei-Feng Chen, Quan-Lin Li, Shuo Wang, Ping-Hong Zhou  

**一句话要点**：提出GI-Bench基准，系统评估多模态大语言模型在胃肠内窥镜临床工作流中的性能与临床标准对比。

**关键词**：多模态大语言模型, 胃肠内窥镜, 临床基准评估, 空间定位瓶颈, 流畅性-准确性悖论, 动态排行榜

## 3 点简述
- 核心问题：多模态大语言模型在胃肠内窥镜中的性能与临床工作流和人类基准对比未经验证。
- 方法要点：构建涵盖20种病变类别的GI-Bench基准，评估12个模型在五阶段临床工作流中的表现。
- 实验或效果：模型在诊断推理中媲美初级内镜医师，但在空间定位和事实准确性上存在瓶颈与矛盾。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) show promise in gastroenterology, yet their performance against comprehensive clinical workflows and human benchmarks remains unverified. To systematically evaluate state-of-the-art MLLMs across a panoramic gastrointestinal endoscopy workflow and determine their clinical utility compared with human endoscopists. We constructed GI-Bench, a benchmark encompassing 20 fine-grained lesion categories. Twelve MLLMs were evaluated across a five-stage clinical workflow: anatomical localization, lesion identification, diagnosis, findings description, and management. Model performance was benchmarked against three junior endoscopists and three residency trainees using Macro-F1, mean Intersection-over-Union (mIoU), and multi-dimensional Likert scale. Gemini-3-Pro achieved state-of-the-art performance. In diagnostic reasoning, top-tier models (Macro-F1 0.641) outperformed trainees (0.492) and rivaled junior endoscopists (0.727; p>0.05). However, a critical "spatial grounding bottleneck" persisted; human lesion localization (mIoU >0.506) significantly outperformed the best model (0.345; p<0.05). Furthermore, qualitative analysis revealed a "fluency-accuracy paradox": models generated reports with superior linguistic readability compared with humans (p<0.05) but exhibited significantly lower factual correctness (p<0.05) due to "over-interpretation" and hallucination of visual features.GI-Bench maintains a dynamic leaderboard that tracks the evolving performance of MLLMs in clinical endoscopy. The current rankings and benchmark results are available at https://roterdl.github.io/GIBench/.

