---
layout: default
title: LSVOS 2025 Challenge Report: Recent Advances in Complex Video Object Segmentation
---

# LSVOS 2025 Challenge Report: Recent Advances in Complex Video Object Segmentation
**arXiv**：[2510.11063v1](https://arxiv.org/abs/2510.11063) · [PDF](https://arxiv.org/pdf/2510.11063.pdf)  
**作者**：Chang Liu, Henghui Ding, Kaining Ying, Lingyi Hong, Ning Xu, Linjie Yang, Yuchen Fan, Mingqi Gao, Jingkun Chen, Yunqi Miao, Gengshen Wu, Zhijin Qin, Jungong Han, Zhixiong Zhang, Shuangrui Ding, Xiaoyi Dong, Yuhang Zang, Yuhang Cao, Jiaqi Wang, Chang Soo Lim, Joonyoung Moon, Donghyeon Cho, Tingmin Li, Yixuan Li, Yang Yang, An Yan, Leilei Cao, Feng Lu, Ran Hong, Youhai Jiang, Fengjie Zhu, Yujie Xie, Hongyang Zhang, Zhihui Liu, Shihai Ruan, Quanzhu Niu, Dengxian Gong, Shihao Chen, Tao Zhang, Yikang Zhou, Haobo Yuan, Lu Qi, Xiangtai Li, Shunping Ji, Ran Hong, Feng Lu, Leilei Cao, An Yan, Alexey Nekrasov, Ali Athar, Daan de Geus, Alexander Hermans, Bastian Leibe  

**一句话要点**：报告LSVOS 2025挑战赛进展，引入复杂视频对象分割新赛道以提升真实场景鲁棒性。

**关键词**：视频对象分割, 复杂场景鲁棒性, 多模态语言模型, 记忆感知传播, 挑战赛报告, 长期一致性

## 3 点简述
- 核心问题：视频对象分割在复杂场景中面临小对象密集、频繁消失重现、严重遮挡及恶劣天气等挑战。
- 方法要点：新增MOSEv2赛道，采用J&Ḟ指标评估多尺度和消失情况，强调LLM/MLLM组件和记忆感知传播。
- 实验或效果：总结数据集、协议和顶尖方案，推动语言感知视频分割在野外环境中的未来发展。

## 摘要（原文）

> This report presents an overview of the 7th Large-scale Video Object
> Segmentation (LSVOS) Challenge held in conjunction with ICCV 2025. Besides the
> two traditional tracks of LSVOS that jointly target robustness in realistic
> video scenarios: Classic VOS (VOS), and Referring VOS (RVOS), the 2025 edition
> features a newly introduced track, Complex VOS (MOSEv2). Building upon prior
> insights, MOSEv2 substantially increases difficulty, introducing more
> challenging but realistic scenarios including denser small objects, frequent
> disappear/reappear events, severe occlusions, adverse weather and lighting,
> etc., pushing long-term consistency and generalization beyond curated
> benchmarks. The challenge retains standard ${J}$, $F$, and ${J\&F}$ metrics for
> VOS and RVOS, while MOSEv2 adopts ${J\&\dot{F}}$ as the primary ranking metric
> to better evaluate objects across scales and disappearance cases. We summarize
> datasets and protocols, highlight top-performing solutions, and distill
> emerging trends, such as the growing role of LLM/MLLM components and
> memory-aware propagation, aiming to chart future directions for resilient,
> language-aware video segmentation in the wild.

