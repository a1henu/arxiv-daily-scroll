---
layout: default
title: A DeepSeek-Powered AI System for Automated Chest Radiograph Interpretation in Clinical Practice
---

# A DeepSeek-Powered AI System for Automated Chest Radiograph Interpretation in Clinical Practice
**arXiv**：[2512.20344v1](https://arxiv.org/abs/2512.20344) · [PDF](https://arxiv.org/pdf/2512.20344.pdf)  
**作者**：Yaowei Bai, Ruiheng Zhang, Yu Lei, Xuhua Duan, Jingfeng Yao, Shuguang Ju, Chaoyang Wang, Wei Yao, Yiwan Guo, Guilin Zhang, Chao Wan, Qian Yuan, Lei Chen, Wenjuan Tang, Biqiang Zhu, Xinggang Wang, Tao Sun, Wei Zhou, Dacheng Tao, Yongchao Xu, Chuansheng Zheng, Huangxuan Zhao, Bo Du  

**一句话要点**：提出基于DeepSeek Janus-Pro的Janus-Pro-CXR系统，用于临床胸片自动解读以缓解放射科医生短缺。

**关键词**：胸片解读, 多模态大语言模型, 前瞻性临床验证, 报告生成, 轻量架构, 开源框架

## 3 点简述
- 全球放射科医生短缺，胸片工作量巨大，现有AI模型缺乏前瞻性临床验证。
- 开发Janus-Pro-CXR系统，通过轻量架构和领域优化，提升报告生成和关键发现检测性能。
- 多中心前瞻性试验显示，系统提高报告质量，减少解读时间18.3%，专家偏好率54.3%。

## 摘要（原文）

> A global shortage of radiologists has been exacerbated by the significant volume of chest X-ray workloads, particularly in primary care. Although multimodal large language models show promise, existing evaluations predominantly rely on automated metrics or retrospective analyses, lacking rigorous prospective clinical validation. Janus-Pro-CXR (1B), a chest X-ray interpretation system based on DeepSeek Janus-Pro model, was developed and rigorously validated through a multicenter prospective trial (NCT07117266). Our system outperforms state-of-the-art X-ray report generation models in automated report generation, surpassing even larger-scale models including ChatGPT 4o (200B parameters), while demonstrating reliable detection of six clinically critical radiographic findings. Retrospective evaluation confirms significantly higher report accuracy than Janus-Pro and ChatGPT 4o. In prospective clinical deployment, AI assistance significantly improved report quality scores, reduced interpretation time by 18.3% (P < 0.001), and was preferred by a majority of experts in 54.3% of cases. Through lightweight architecture and domain-specific optimization, Janus-Pro-CXR improves diagnostic reliability and workflow efficiency, particularly in resource-constrained settings. The model architecture and implementation framework will be open-sourced to facilitate the clinical translation of AI-assisted radiology solutions.

