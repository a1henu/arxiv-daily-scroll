---
layout: default
title: HyperPriv-EPN: Hypergraph Learning with Privileged Knowledge for Ependymoma Prognosis
---

# HyperPriv-EPN: Hypergraph Learning with Privileged Knowledge for Ependymoma Prognosis
**arXiv**：[2601.00626v1](https://arxiv.org/abs/2601.00626) · [PDF](https://arxiv.org/pdf/2601.00626.pdf)  
**作者**：Shuren Gabriel Yu, Sikang Ren, Yongji Tian  

**一句话要点**：提出HyperPriv-EPN，基于超图学习与特权知识，解决室管膜瘤术前预后挑战。

**关键词**：室管膜瘤预后, 超图学习, 特权信息学习, 双流蒸馏, 医学影像分析

## 3 点简述
- 核心问题：室管膜瘤术前预后困难，因MRI缺乏术后文本的语义信息，且推理时文本不可用。
- 方法要点：采用超图学习与特权信息学习框架，通过割裂图策略和双流蒸馏，使学生图从视觉特征中模拟语义结构。
- 实验或效果：在311名患者多中心队列中验证，实现最先进的诊断准确性和生存分层。

## 摘要（原文）

> Preoperative prognosis of Ependymoma is critical for treatment planning but challenging due to the lack of semantic insights in MRI compared to post-operative surgical reports. Existing multimodal methods fail to leverage this privileged text data when it is unavailable during inference. To bridge this gap, we propose HyperPriv-EPN, a hypergraph-based Learning Using Privileged Information (LUPI) framework. We introduce a Severed Graph Strategy, utilizing a shared encoder to process both a Teacher graph (enriched with privileged post-surgery information) and a Student graph (restricted to pre-operation data). Through dual-stream distillation, the Student learns to hallucinate semantic community structures from visual features alone. Validated on a multi-center cohort of 311 patients, HyperPriv-EPN achieves state-of-the-art diagnostic accuracy and survival stratification. This effectively transfers expert knowledge to the preoperative setting, unlocking the value of historical post-operative data to guide the diagnosis of new patients without requiring text at inference.

