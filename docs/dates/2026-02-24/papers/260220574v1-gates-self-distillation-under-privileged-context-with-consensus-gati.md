---
layout: default
title: GATES: Self-Distillation under Privileged Context with Consensus Gating
---

# GATES: Self-Distillation under Privileged Context with Consensus Gating
**arXiv**：[2602.20574v1](https://arxiv.org/abs/2602.20574) · [PDF](https://arxiv.org/pdf/2602.20574.pdf)  
**作者**：Alex Stein, Furong Huang, Tom Goldstein  

**一句话要点**：提出共识门控轨迹蒸馏方法，在无可靠监督的文档问答中提升学生模型性能。

**关键词**：自蒸馏, 文档问答, 共识门控, 轨迹蒸馏, 无监督学习

## 3 点简述
- 核心问题：文档问答中缺乏真实标签或外部评估，传统自蒸馏依赖导师模型正确性假设不可靠。
- 方法要点：通过采样多个导师推理轨迹，利用共识作为可靠性信号门控学习，蒸馏完整轨迹而非仅最终答案。
- 实验或效果：在非对称评估下，领域内准确率从46.0%提升至62.0%，公开数学基准平均准确率从20.2%提升至35.4%。

## 摘要（原文）

> We study self-distillation in settings where supervision is unreliable: there are no ground truth labels, verifiable rewards, or external graders to evaluate answers. We focus on document-grounded question answering with asymmetric context, where a single model serves as both tutor (with access to a relevant source document during training) and student (answering from the question alone at test time). Rather than assuming tutor correctness, we derive supervision online from tutor consensus by sampling multiple document-grounded reasoning traces and using agreement to gate learning. Conditioned on this reliability signal, we distill knowledge through full tutor reasoning trajectories (not just final answers), providing a dense and stable learning signal. Empirically, this consensus-gated trajectory distillation substantially improves transfer to the document-free student. Held-out in-domain accuracy under asymmetric evaluation improves from 46.0\% to 62.0\%, and average (maj@8) accuracy on public document-free math benchmarks improves from 20.2\% to 35.4\%.

