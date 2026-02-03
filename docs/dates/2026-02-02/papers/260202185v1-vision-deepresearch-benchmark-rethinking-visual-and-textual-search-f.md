---
layout: default
title: Vision-DeepResearch Benchmark: Rethinking Visual and Textual Search for Multimodal Large Language Models
---

# Vision-DeepResearch Benchmark: Rethinking Visual and Textual Search for Multimodal Large Language Models
**arXiv**：[2602.02185v1](https://arxiv.org/abs/2602.02185) · [PDF](https://arxiv.org/pdf/2602.02185.pdf)  
**作者**：Yu Zeng, Wenxuan Huang, Zhen Fang, Shuang Chen, Yufan Shen, Yishuo Cai, Xiaoman Wang, Zhenfei Yin, Lin Chen, Zehui Chen, Shiting Huang, Yiming Zhao, Yao Hu, Philip Torr, Wanli Ouyang, Shaosheng Cao  

**一句话要点**：提出Vision-DeepResearch基准以评估多模态大语言模型在真实视觉-文本搜索场景中的能力

**关键词**：多模态大语言模型, 视觉-文本搜索, 基准评估, 视觉检索, VQA, 深度学习系统

## 3 点简述
- 现有基准存在视觉搜索中心性不足和评估场景过于理想化的问题
- 构建包含2000个VQA实例的VDR-Bench，通过多阶段策划和专家评审确保真实性
- 提出多轮裁剪搜索工作流，有效提升模型在真实视觉检索场景中的性能

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have advanced VQA and now support Vision-DeepResearch systems that use search engines for complex visual-textual fact-finding. However, evaluating these visual and textual search abilities is still difficult, and existing benchmarks have two major limitations. First, existing benchmarks are not visual search-centric: answers that should require visual search are often leaked through cross-textual cues in the text questions or can be inferred from the prior world knowledge in current MLLMs. Second, overly idealized evaluation scenario: On the image-search side, the required information can often be obtained via near-exact matching against the full image, while the text-search side is overly direct and insufficiently challenging. To address these issues, we construct the Vision-DeepResearch benchmark (VDR-Bench) comprising 2,000 VQA instances. All questions are created via a careful, multi-stage curation pipeline and rigorous expert review, designed to assess the behavior of Vision-DeepResearch systems under realistic real-world conditions. Moreover, to address the insufficient visual retrieval capabilities of current MLLMs, we propose a simple multi-round cropped-search workflow. This strategy is shown to effectively improve model performance in realistic visual retrieval scenarios. Overall, our results provide practical guidance for the design of future multimodal deep-research systems. The code will be released in https://github.com/Osilly/Vision-DeepResearch.

